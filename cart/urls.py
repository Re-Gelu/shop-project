from django.urls import path, re_path
from django.contrib.auth.views import *
from . import views

urlpatterns = [
    path(
        'cart_add_one/<int:product_id>/',
        views.CartAddOneRedirectView.as_view(),
        name='cart_add_one'
    ),
    path(
        'cart_remove_one/<int:product_id>/',
        views.CartRemoveOneRedirectView.as_view(),
        name='cart_remove_one'
    ),
    path(
        'cart_remove/<int:product_id>/',
        views.CartRemoveRedirectView.as_view(),
        name='cart_remove'
    )
]
