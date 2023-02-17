from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from extra_settings.models import Setting
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from .QIWI import get_QIWI_p2p

from .models import *
from .forms import *

from shop.models import *
from shop.views import CustomTemplateView

from cart.cart import cart


@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class OrderPageView(LoginRequiredMixin, CustomTemplateView):
    """ Order page class view """
    
    template_name = "order.html"
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_form"] = SubmitOrder()
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        cart = cart(request)
        form = SubmitOrder(request.POST or None)
        if form.is_valid():
            p2p = get_QIWI_p2p()
            if p2p == None:
                
                # Если нет или не прошел проверку ключ QIWI
                return HttpResponse(
                    f"""
                        <center><h3>SET QIWI_PRIVATE_KEY SETTING IN Settings on admin page or settings.py file or .env.prod FILE!!!</h3></center>
                        <hr>
                        <center><small>with love from Re;Gelu :3</small></center>
                    """
                )
            else:
                cd = form.cleaned_data
                new_order = orders()

                # Создание объекта нового заказа
                new_order.user_id = request.user.id
                new_order.adress = f"Адрес: {cd['adress']}"
                new_order.contacts = f"Номер телефона: {cd['phone_number']}"

                new_order.product_info = ""
                product_list = {}
                for key, item in enumerate(cart):
                    new_order.product_info += f"\n{key + 1}) ID товара: {item['id']}, Наименование товара: {item['name']}"
                    new_order.product_info += f", Общая стоимость товара: {item['total_promo_price']}$" if 'total_promo_price' in item else f", Общая стоимость товара: {item['total_price']}$"
                    product_list[key] = item

                new_order.product_info += f"\n\nИТОГО: {cart.get_total_promo_price()} RUB"
                new_order.cart = product_list

                # Создание QIWI платежа
                site_name = Setting.get("SITE_NAME")
                successUrl = "http://62.217.178.182:1337/dashboard/"
                bill = p2p.bill(
                    bill_id=new_order.UUID,
                    #amount=cart.get_total_promo_price(),
                    amount=1,
                    lifetime=Setting.get("QIWI_PAYMENTS_LIFETIME"),
                    comment=f"{site_name} - Заказ №{new_order.UUID}"
                )

                new_order.save()
                cart.clear()
                return redirect(bill.pay_url + f"&successUrl={successUrl}")
        else:
            context = self.get_context_data()
            context["submit_form"] = form
            return render(request, self.template_name, context=context)
