from django.urls import path, re_path
from django.contrib.auth.views import *
from django.views.generic import RedirectView
from .forms import *
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'products/',
        views.products_page,
        name='products'
    ),
    path(
        'product/',
        views.product,
        name='product'
    ),
    path(
        'promo/',
        views.promo,
        name='promo'
    ),
    path(
        'contacts/',
        views.contacts,
        name='contacts'
    ),
    path(
        'about/',
        views.about,
        name='about'
    ),
    path(
        'delivery/',
        views.delivery,
        name='delievery'
    ),
    path(
        'dashboard/',
        views.dashboard,
        name="dashboard"
    ),

    path(
        'db_auto_fill/<int:amount>/<model>/',
        views.db_auto_fill,
        name='db_auto_fill'
    ),
]