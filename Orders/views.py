from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded

from Site.celery import app

from .models import *
from .forms import *

from Shop.models import *

from Cart.cart import Cart
from Cart.forms import *

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

#latest_order_id = 0

#@app.task
@login_required
def order(request):
    cart = Cart(request)
    form = Submit_order(request.POST)
    if request.method == "POST" and form.is_valid():
        cd = form.cleaned_data
        new_order = Orders()

        new_order.user_id = request.user.id
        new_order.adress = f"Адрес: {cd['adress']}"
        new_order.contacts = f"Номер телефона: {cd['phone_number']}"

        #new_order.product_list = f"Короткий UUID заказа: {new_order.UUID}\n"
        new_order.product_info = ""
        product_list = {}
        for key, item in enumerate(cart):
            new_order.product_info += f"\n{key + 1}) ID товара: {item['id']}, Наименование товара: {item['name']}"
            new_order.product_info += f", Общая стоимость товара: {item['total_promo_price']}$" if 'total_promo_price' in item else f", Общая стоимость товара: {item['total_price']}$"
            product_list[key] = item

        new_order.product_info += f"\n\nИТОГО: {cart.get_total_promo_price()}$"
        new_order.order_cart = product_list
        
        context = {
            'UUID': new_order.UUID,
        }
        context.update(get_base_context_data(request))
        #return render(request, "submit_order.html", context=context)
        
        # Create Payment object
        Payment = get_payment_model()
        payment = Payment.objects.create(
            variant='default',
            description='Test purchase',
            total=Decimal(cart.get_total_promo_price()),
            tax=Decimal(0),
            currency='USD',
            delivery=Decimal(1),
            billing_first_name='Sherlock',
            billing_last_name='Holmes',
            billing_address_1='221B Baker Street',
            billing_address_2='',
            billing_city='London',
            billing_postcode='NW1 6XE',
            billing_country_code='GB',
            billing_country_area='Greater London',
            customer_ip_address='127.0.0.1',
        )
        
        # Set Payment order_UUID DB field
        Payment.objects.filter(pk=payment.id).update(order_UUID=payment.id)
        
        # Get Payment object
        payment = get_object_or_404(get_payment_model(), id=payment.id)
        
        try:
            form = payment.get_form(data=request.POST or None)
        except RedirectNeeded as redirect_to:
            return redirect(str(redirect_to))
        
        #new_order.save()
        #cart.clear()

        context = {
            'form': form,
            'payment': payment
        }
        
        context.update(get_base_context_data(request))

        return render(request, 'payment.html', context=context)
    
    else:
        submit_form = Submit_order()
        context = {
            "submit_form": submit_form
        }
        context.update(get_base_context_data(request))
        return render(request, "order.html", context=context)