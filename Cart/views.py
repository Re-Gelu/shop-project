from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from Shop.models import Products
from .cart import Cart
from .forms import Cart_add_one_product_form

@require_POST
def cart_action(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = Cart_add_one_product_form(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.action(product=product, product_action=cd['product_add_or_remove_one'])

    return redirect(request.META.get('HTTP_REFERER'))

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    
    return redirect(request.META.get('HTTP_REFERER'))

def cart_detail(request):
    cart = Cart(request)
    
    return render(request, 'dashboard.html', {'cart': cart})