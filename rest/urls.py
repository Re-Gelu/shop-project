from django.urls import path, include
from rest_framework import routers
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

# Router
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'subcategories', SubcategoriesViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),

    path(
        'auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    
    path(
        'header_offcanvas_body/',
        HeaderOffcanvasBodyView.as_view()
    ),
    
    path(
        'dashboard_cart/',
        DashboardCartView.as_view()
    )
]

""" rest_urlpatterns = [
    re_path(
        r'cart/',
        CartAPIView.as_view(),
    ),
]

urlpatterns += format_suffix_patterns(rest_urlpatterns) """
