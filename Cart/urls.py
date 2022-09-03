from django.urls import path, re_path
from django.contrib.auth.views import *
from .forms import *
from . import views

urlpatterns = [
    path(
        'cart/',
        views.cart_detail,
        name='cart_detail'
    ),
    path(
        'cart_action/<int:product_id>/',
        views.cart_action,
        name='cart_action'
    ),
    path(
        'cart_remove/<int:product_id>/',
        views.cart_remove,
        name='cart_remove'
    )
]
