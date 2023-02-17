from django.urls import re_path
from django.contrib.auth.views import *
from django.views.decorators.cache import cache_page
from django.conf import settings
from allauth.account.views import LoginView
from .forms import *
from . import views

urlpatterns = [
    re_path(
        r'^login/$',
        cache_page(settings.CACHING_TIME)(LoginView.as_view(template_name="login.html", form_class=LoginForm)),
        name='login'
    ),
    re_path(
        r'^logout/$',
        cache_page(settings.CACHING_TIME)(LogoutView.as_view(template_name="logout.html")),
        name='logout'
    ),
    re_path(
        r'^registration/$',
        cache_page(settings.CACHING_TIME)(views.RegistrationPageView.as_view()),
        name='registration'
    ),
    re_path(
        r'^registration/$',
        cache_page(settings.CACHING_TIME)(views.RegistrationPageView.as_view()),
        name='account_signup'
    ),
    re_path(
        r'^password_change/$',
        cache_page(settings.CACHING_TIME)(PasswordChangeView.as_view(template_name="change_password.html", form_class=ChangePassword)),
        name='password_change'
    ),
    re_path(
        r'^password_change_done/$',
        cache_page(settings.CACHING_TIME)(PasswordChangeDoneView.as_view(template_name="change_password_done.html")),
        name="password_change_done"
    )
]


""" # django-allauth URLS
    path(
        'accounts/', 
        include('allauth.urls')
    ), """
