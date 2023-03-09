from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/header_offcanvas_body/',
        views.HeaderOffcanvasBodyView.as_view(),
        name='header_offcanvas_body'
    ),
    path(
        'api/dashboard_cart/',
        views.DashboardCartView.as_view(),
        name='dashboard_cart'
    ),
]
