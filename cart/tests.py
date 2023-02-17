from django.test import TestCase
from django.urls import reverse, resolve

from shop.models import Products

from .cart import Cart
from .views import *

class CartViewsTests(TestCase):
    
    def setUp(self):
        self.product = Products.objects.create(
            name='test product',
            price=200,
            promo_price=250,
            stock=100,
            available=True
        )
        self.cart = Cart(self.client)
        self.url_1 = reverse('cart_add_one', args=(1, ))
        self.response_1 = self.client.get(self.url_1)
        self.url_2 = reverse('cart_remove_one', args=(1, ))
        self.response_2 = self.client.get(self.url_2)
        self.url_3 = reverse('cart_remove', args=(1, ))
        self.response_23 = self.client.get(self.url_3)
    
    # cart redirect views tests
    def test_cart_add_one_redirect_page_status_code(self):
        self.assertEqual(self.response_1.status_code, 302)
        
    def test_cart_add_one_redirect_page_resolves_CartAddOneRedirectView(self):
        view = resolve(self.url_1)
        self.assertEqual(
            view.func.__name__,
            CartAddOneRedirectView.as_view().__name__
        )
        
    def test_cart_remove_one_redirect_page_status_code(self):
        self.assertEqual(self.response_2.status_code, 302)

    def test_cart_remove_one_redirect_page_resolves_CartAddOneRedirectView(self):
        view = resolve(self.url_2)
        self.assertEqual(
            view.func.__name__,
            CartRemoveOneRedirectView.as_view().__name__
        )
    
    def test_cart_remove_redirect_page_status_code(self):
        self.assertEqual(self.response_2.status_code, 302)

    def test_cart_remove_redirect_page_resolves_CartAddOneRedirectView(self):
        view = resolve(self.url_2)
        self.assertEqual(
            view.func.__name__,
            CartRemoveOneRedirectView.as_view().__name__
        )

class CartTests(TestCase):
    
    def setUp(self):
        self.product = Products.objects.create(
            name='test product',
            price=200,
            promo_price=250,
            stock=100,
            available=True
        )
        self.cart = Cart(self.client)

    def test_cart_actions(self):
        self.cart.action(self.product, 5, True)
        self.assertEqual(len(self.cart), 5)
        self.cart.action(self.product, 2, False)
        self.assertEqual(len(self.cart), 3)
        self.assertEqual(self.cart.get_total_price(), 600)
        self.assertEqual(self.cart.get_total_promo_price(), 600)
        self.cart.remove(self.product)
        self.assertEqual(self.cart.get_total_promo_price(), 0)
        self.assertEqual(len(self.cart), 0)