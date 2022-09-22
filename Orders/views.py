from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Site.celery_tasks import app

from .models import *
from .forms import *

from Shop.models import *

from Cart.cart import Cart
from Cart.forms import *

# Get base context values


@app.task
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


@app.task
@login_required
def order(request):
    cart = Cart(request)
    form = Submit_order(request.POST)
    if request.method == "POST" and form.is_valid():
        cd = form.cleaned_data
        new_order = Orders()

        new_order.adress = f"Адрес: {cd['adress']}"
        new_order.contacts = f"Номер телефона: {cd['phone_number']}"

        new_order.product_list = f"Короткий UUID заказа: {new_order.UUID}\n"
        for key, item in enumerate(cart):
            new_order.product_list += f"\n{key + 1}) ID товара: {item['id']}, Наименование товара: {item['name']}"
            new_order.product_list += f", Общая стоимость товара: {item['total_promo_price']}$" if 'total_promo_price' in item else f", Общая стоимость товара: {item['total_price']}$"

        new_order.product_list += f"\n\nИТОГО: {cart.get_total_promo_price()}$"

        print(new_order.product_list)
        print(new_order.adress)
        print(new_order.contacts)

        new_order.save()
        cart.clear()
        
        context = {
            'UUID': new_order.UUID,
        }
        context.update(get_base_context_data(request))
        return render(request, "submit_order.html", context=context)
    else:
        submit_form = Submit_order()
        context = {
            "submit_form": submit_form
        }
        context.update(get_base_context_data(request))
        return render(request, "order.html", context=context)