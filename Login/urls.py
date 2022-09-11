from django.urls import re_path
from django.contrib.auth.views import *
from Shop.forms import *
from . import views

urlpatterns = [
    re_path(
        r'^login/$',
        LoginView.as_view(template_name="login.html",
                          authentication_form=LoginForm),
        name='login'
    ),
    re_path(
        r'^logout/$',
        LogoutView.as_view(template_name="logout.html"),
        name='logout'
    ),
    re_path(
        r'^registration/$',
        views.registration,
        name='registration'
    ),
    re_path(
        r'^password_change/$',
        PasswordChangeView.as_view(
            template_name="change_password.html", form_class=ChangePassword),
        name='password_change'
    ),
    re_path(
        r'^password_change_done/$',
        PasswordChangeDoneView.as_view(
            template_name="change_password_done.html"),
        name="password_change_done"
    ),
]
