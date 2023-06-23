from django.urls import path
from . import viewsets

urlpatterns = [
    path(
        'api/header_offcanvas_body/',
        viewsets.HeaderOffcanvasBodyView.as_view(),
        name='header_offcanvas_body'
    ),
    path(
        'api/dashboard_cart/',
        viewsets.DashboardCartView.as_view(),
        name='dashboard_cart'
    ),
]
