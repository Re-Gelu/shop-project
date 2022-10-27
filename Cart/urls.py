from django.urls import path, re_path
from django.contrib.auth.views import *
from .forms import *
from . import views

urlpatterns = [
    path(
        'cart_action/<int:product_id>/',
        views.CartActionRedirectView.as_view(),
        name='cart_action'
    ),
    path(
        'cart_remove/<int:product_id>/',
        views.CartRemoveRedirectView.as_view(),
        name='cart_remove'
    )
]
