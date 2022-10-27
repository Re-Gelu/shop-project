from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect

from Shop.models import Products
from .cart import Cart
from .forms import Cart_add_one_product_form


class CartActionRedirectView(RedirectView):
    """ Add or remove one product in cart class view """
    
    def get_redirect_url(self, *args, **kwargs):
        return self.request.META.get('HTTP_REFERER')

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Products, id=kwargs.get("product_id"))
        form = Cart_add_one_product_form(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            cart.action(product=product,product_action=cd['product_add_or_remove_one'])

        return self.get(request, *args, **kwargs)

class CartRemoveRedirectView(RedirectView):
    """ Remove product from cart class view """
    
    def get_redirect_url(self, *args, **kwargs):
        return self.request.META.get('HTTP_REFERER')
    
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Products, id=kwargs.get("product_id"))
        cart.remove(product)

        return HttpResponseRedirect(self.get_redirect_url())