from decimal import Decimal
from django.conf import settings
from Shop.models import *
from rest_framework.serializers import ModelSerializer

class Cart:
    
    class ProductSerializer(ModelSerializer):

        class Meta:
            model = Products
            fields = ("id", "name", "price", "promo_price", "image", "stock", "available")
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session 
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
            
    def __iter__(self):
        for item in self.cart.values():
            yield item

    def __len__(self):
        return sum(item['product_amount'] for item in self.cart.values())
        
    def action(self, product, product_amount:int=1, product_action=True):
        product_id = str(product.id)
        
        # Product in cart set with base data from product model
        if product_id not in self.cart:
            product = Products.objects.get(id=product_id)
            self.cart[product_id] = self.ProductSerializer(product).data
            self.cart[product_id]['product_amount'] = 0
        
        # Product amount set
        self.cart[product_id]['product_amount'] += product_amount if product_action else -product_amount
        
        # Cart limits check
        if not self.cart[product_id]['available']:
            self.remove(product)
        elif self.cart[product_id]['product_amount'] > settings.MAX_PRODUCT_AMOUNT_IN_CART:
            self.cart[product_id]['product_amount'] = settings.MAX_PRODUCT_AMOUNT_IN_CART
        elif self.cart[product_id]['product_amount'] < settings.MIN_PRODUCT_AMOUNT_IN_CART:
            self.remove(product) 
        elif not settings.MIN_PRODUCTS_IN_CART <= len(self.cart) <= settings.MAX_PRODUCTS_IN_CART:
            self.remove(product)  
        else:
            # Total price set
            self.cart[product_id]['total_price'] = str(Decimal(self.cart[product_id]['price']) *  self.cart[product_id]['product_amount'])

            if self.cart[product_id]['promo_price']:
                self.cart[product_id]['total_promo_price'] = str(Decimal(self.cart[product_id]['promo_price']) *  self.cart[product_id]['product_amount'])

        self.save()
        
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['product_amount'] for item in self.cart.values())
        
    def get_total_promo_price(self):        
        return sum(Decimal(item['total_promo_price']) if item['promo_price'] else Decimal(item['total_price']) for item in self.cart.values())
        
    def clear(self):
        # delete the session cart
        del self.session[settings.CART_SESSION_ID]
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True
        
    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True
