from django.urls import re_path
from django.contrib.auth.views import *
from allauth.account.views import LoginView
from .forms import *
from . import views

urlpatterns = [
    re_path(
        r'^login/$',
        LoginView.as_view(template_name="login.html", form_class=LoginForm),
        name='login'
    ),
    re_path(
        r'^logout/$',
        LogoutView.as_view(template_name="logout.html"),
        name='logout'
    ),
    re_path(
        r'^registration/$',
        views.RegistrationPageView.as_view(),
        name='registration'
    ),
    re_path(
        r'^registration/$',
        views.RegistrationPageView.as_view(),
        name='account_signup'
    ),
    re_path(
        r'^password_change/$',
        PasswordChangeView.as_view(template_name="change_password.html", form_class=ChangePassword),
        name='password_change'
    ),
    re_path(
        r'^password_change_done/$',
        PasswordChangeDoneView.as_view(template_name="change_password_done.html"),
        name="password_change_done"
    )
]


""" # django-allauth URLS
    path(
        'accounts/', 
        include('allauth.urls')
    ), """
