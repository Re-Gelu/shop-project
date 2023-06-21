from django.urls import path
from django.contrib.auth.views import *
from django.views.decorators.cache import cache_page
from django.conf import settings
from allauth.account.views import LoginView
from .forms import *
from . import views

urlpatterns = [
    path(
        'login',
        cache_page(settings.CACHING_TIME)(
            LoginView.as_view(template_name="login.html", form_class=LoginForm)
        ),
        name='custom_login'
    ),
    path(
        'logout',
        cache_page(settings.CACHING_TIME)(
            LogoutView.as_view(template_name="logout.html")
        ),
        name='custom_logout'
    ),
    path(
        'registration',
        cache_page(settings.CACHING_TIME)(
            views.RegistrationPageView.as_view()
        ),
        name='custom_registration'
    ),
    path(
        'registration',
        cache_page(settings.CACHING_TIME)(
            views.RegistrationPageView.as_view()
        ),
        name='account_signup'
    ),
    path(
        'password_change',
        cache_page(settings.CACHING_TIME)(
            PasswordChangeView.as_view(
                template_name="change_password.html",
                form_class=ChangePassword
            )
        ),
        name='custom_password_change'
    ),
    path(
        'password_change_done',
        cache_page(settings.CACHING_TIME)(
            PasswordChangeDoneView.as_view(
                template_name="change_password_done.html"
            )
        ),
        name="custom_password_change_done"
    )
]
