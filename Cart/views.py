from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect

from Shop.models import Products
from .cart import Cart

class CartAddOneRedirectView(RedirectView):
    """ Add one product in cart class view """

    def get_redirect_url(self, *args, **kwargs):
        return self.request.META.get('HTTP_REFERER')

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Products, id=kwargs.get("product_id"))
        
        cart.action(product=product, action=True)

        return HttpResponseRedirect(self.get_redirect_url())

class CartRemoveOneRedirectView(RedirectView):
    """ remove one product in cart class view """

    def get_redirect_url(self, *args, **kwargs):
        return self.request.META.get('HTTP_REFERER')

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Products, id=kwargs.get("product_id"))

        cart.action(product=product, action=False)

        return HttpResponseRedirect(self.get_redirect_url())

class CartRemoveRedirectView(RedirectView):
    """ Remove product from cart class view """
    
    def get_redirect_url(self, *args, **kwargs):
        return self.request.META.get('HTTP_REFERER')
    
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Products, id=kwargs.get("product_id"))
        cart.remove(product)

        return HttpResponseRedirect(self.get_redirect_url())