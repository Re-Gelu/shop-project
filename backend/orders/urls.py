from django.urls import path
from . import views

urlpatterns = [
    path(
        'order/',
        views.OrderPageView.as_view(),
        name='order'
    ),
]
