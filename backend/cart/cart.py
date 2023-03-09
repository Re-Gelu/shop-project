from decimal import Decimal
from django.conf import settings
from shop.models import *
from rest_framework.serializers import ModelSerializer
from .serializers import CartSerializer


class Cart:

    class ProductSerializer(ModelSerializer):

        class Meta:
            model = Products
            fields = ("id", "name", "price", "promo_price",
                      "image", "stock", "available")

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

    def get_cart_list(self):
        list = CartSerializer(data=[item for item in self.cart.values()])
        return list.initial_data

    def action(self, product: Products, amount: int = 1, action: bool = True):
        product_id = str(product.id)

        # Product in cart set with base data from product model
        if product_id not in self.cart:
            product = Products.objects.get(id=product_id)
            self.cart[product_id] = self.ProductSerializer(product).data
            self.cart[product_id]['product_amount'] = 0

        # Set product amount
        self.cart[product_id]['product_amount'] += amount if action else -amount

        # If is available
        if not self.cart[product_id]['available']:
            return self.remove(product)

        # If product_amount >= stock of product
        if self.cart[product_id]['product_amount'] >= self.cart[product_id]['stock']:
            self.cart[product_id]['product_amount'] = self.cart[product_id]['stock']

        # Check if the quantity of the product is correct
        if self.cart[product_id]['product_amount'] > settings.MAX_PRODUCT_AMOUNT_IN_CART:
            self.cart[product_id]['product_amount'] = settings.MAX_PRODUCT_AMOUNT_IN_CART
        elif self.cart[product_id]['product_amount'] < settings.MIN_PRODUCT_AMOUNT_IN_CART:
            return self.remove(product)

        # If cart length is not correct
        if not settings.MIN_PRODUCTS_IN_CART <= len(self.cart) <= settings.MAX_PRODUCTS_IN_CART:
            return self.remove(product)

        # Total price set
        self.cart[product_id]['total_price'] = str(Decimal(
            self.cart[product_id]['price']) * self.cart[product_id]['product_amount'])

        # Set total promo price
        if self.cart[product_id]['promo_price']:
            self.cart[product_id]['total_promo_price'] = str(Decimal(
                self.cart[product_id]['promo_price']) * self.cart[product_id]['product_amount'])

        return self.save()

    def remove(self, product: Products):
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
