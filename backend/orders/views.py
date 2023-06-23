from cart.cart import Cart
from config.qiwi import get_QIWI_p2p
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from extra_settings.models import Setting
from shop.models import *
from shop.views import CustomTemplateView

from .forms import *
from .models import *

# Кэшируются только GET и HEAD ответы со статусом 200
default_decorators = (cache_page(getattr(settings, 'CACHING_TIME', 60)), vary_on_headers("Authorization",))


@method_decorator(default_decorators, name="dispatch")
class OrderPageView(LoginRequiredMixin, CustomTemplateView):
    """ Order page class view """

    template_name = "order.html"
    login_url = 'custom_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_form"] = SubmitOrder()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = SubmitOrder(request.POST or None)
        p2p = get_QIWI_p2p()
        
        if not form.is_valid():
            context = self.get_context_data()
            context["submit_form"] = form
            return render(request, self.template_name, context=context)
        
        if p2p == None:

            # Если ключа QIWI нет или он не прошел проверку
            return HttpResponse(
                f"""
                    <center><h3>Set QIWI_PRIVATE_KEY setting!</h3></center>
                    <hr>
                    <center><small>with love from Re;Gelu :3</small></center>
                """
            )
            
        cd = form.cleaned_data
        new_order = Orders()
        new_order.user_id = request.user.id
        new_order.adress = cd.get('adress')
        new_order.contacts = cd.get('phone_number')
        new_order.cart = list(cart)

        new_order.order_info = ""
        for key, item in enumerate(cart):
            new_order.order_info += f"\n{key + 1}) ID товара: {item.get('id')}, Наименование товара: {item.get('name')}"
            new_order.order_info += f", Общая стоимость товара: {item.get('total_promo_price')}$" if 'total_promo_price' in item else f", Общая стоимость товара: {item.get('total_price')}$"

        new_order.order_info += f"\n\nИТОГО: {cart.get_total_promo_price()} RUB"

        # Создание QIWI платежа
        site_name = Setting.get("SITE_NAME")
        bill = p2p.bill(
            bill_id=new_order.shortuuid,
            amount=cart.get_total_promo_price(),
            lifetime=Setting.get("QIWI_PAYMENTS_LIFETIME"),
            comment=f"{site_name} - Заказ №{new_order.shortuuid}"
        )
        
        success_payment_url = getattr(settings, "SUCCESS_PAYMENT_URL", "")
        
        # Доабавление ссылки на оплату
        new_order.payment_link = bill.pay_url + \
            f"&successUrl={success_payment_url}"
        new_order.save()
        
        cart.clear()
        return redirect(bill.pay_url + f"&successUrl={success_payment_url}")
