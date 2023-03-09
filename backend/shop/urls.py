from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import *
from django.views.decorators.cache import cache_page
from django.conf import settings
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
        'dashboard/',
        views.DashboardPageView.as_view(),
        name="dashboard"
    ),
    path(
        'contacts/',
        cache_page(settings.CACHING_TIME)(
            views.CustomTemplateView.as_view(template_name="contacts.html")
        ),
        name='contacts'
    ),
    path(
        'about/',
        cache_page(settings.CACHING_TIME)(
            views.CustomTemplateView.as_view(template_name="about.html")
        ),
        name='about'
    ),
    path(
        'delivery/',
        cache_page(settings.CACHING_TIME)(
            views.CustomTemplateView.as_view(template_name="delivery.html")
        ),
        name='delivery'
    ),
]
