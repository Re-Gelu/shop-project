from django.urls import path, re_path
from django.contrib.auth.views import *
from .forms import *
from . import views

urlpatterns = [
    path(
        '',
        views.IndexPageView.as_view(),
        name='index'
    ),
    path(
        'products/<str:category>/<str:subcategory>/',
        views.ProductsPageView.as_view(),
        name='products'
    ),
    path(
        'products/<str:category>/',
        views.ProductsPageView.as_view(),
        name='products'
    ),
    path(
        'products/',
        views.ProductsPageView.as_view(),
        name='products'
    ),
    path(
        'product/',
        views.ProductPageView.as_view(),
        name='product'
    ),
    path(
        'contacts/',
        views.CustomTemplateView.as_view(template_name="contacts.html"),
        name='contacts'
    ),
    path(
        'about/',
        views.CustomTemplateView.as_view(template_name="about.html"),
        name='about'
    ),
    path(
        'delivery/',
        views.CustomTemplateView.as_view(template_name="delivery.html"),
        name='delievery'
    ),
    path(
        'dashboard/',
        views.DashboardPageView.as_view(),
        name="dashboard"
    ),

    path(
        'db_auto_fill/<int:amount>/<model>/',
        views.DB_AutoFillView.as_view(),
        name='db_auto_fill'
    ),
]