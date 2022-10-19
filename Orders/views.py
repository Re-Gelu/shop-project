from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from extra_settings.models import Setting
from pyqiwip2p import QiwiP2P
#from .tasks import payment_handler
from Site.celery import app

from .models import *
from .forms import *

from Shop.models import *

from Cart.cart import Cart
from Cart.forms import *

# QIWI payments
try:
    p2p = QiwiP2P(auth_key=Setting.get("QIWI_PRIVATE_KEY"))
except:
    print("[!] SET QIWI_PRIVATE_KEY SETTING IN .env.prod FILE!!!\n")
    p2p = QiwiP2P(auth_key=settings.QIWI_PRIVATE_KEY)

# Get base context values
def get_base_context_data(request):
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    random_product = Products.objects.order_by('?').first()
    cart_remove_one_form = Cart_remove_one_product_form()
    cart_add_one_form = Cart_add_one_product_form()
    cart = Cart(request)

    base_context = {    
        "categories": categories,
        "subcategories": subcategories,
        "random_product": random_product,
        "cart_add_one_form": cart_add_one_form,
        "cart_remove_one_form": cart_remove_one_form,
        "cart": cart
    }

    return base_context

#@app.task
@login_required
def order(request):
    cart = Cart(request)
    form = Submit_order(request.POST)
    if request.method == "POST" and form.is_valid():
        cd = form.cleaned_data
        new_order = Orders()
        
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
        successUrl = "https://vk.com/re_gelu"
        bill = p2p.bill(
            bill_id=new_order.UUID,
            #amount=cart.get_total_promo_price(), 
            amount=1, 
            lifetime=Setting.get("QIWI_PAYMENTS_LIFETIME"),
            comment=f"{site_name} - Заказ №{new_order.UUID}"
        )
        
        new_order.save()
        #cart.clear()
        
        return redirect(bill.pay_url + f"&successUrl={successUrl}")
        
        """ context = {
            'UUID': new_order.UUID,
        }
        
        context.update(get_base_context_data(request))
        return render(request, "submit_order.html", context=context) """
    
    else:
        submit_form = Submit_order()
        context = {
            "submit_form": submit_form
        }
        context.update(get_base_context_data(request))
        return render(request, "order.html", context=context)