from django.contrib.auth.decorators import login_required
from rest_framework.serializers import ModelSerializer
from .models import *
from Cart.cart import Cart

class OrderSerializer(ModelSerializer):
    
    class Meta:
        model = Products
        fields = ("id", "name", "price", "promo_price", "image", "stock", "available")

@login_required
def submit_order(request):
    cart = Cart(request)
    return 0
