from django.urls import path, re_path
from django.contrib.auth.views import *
from .forms import *
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'products/<int:page>/',
        views.products_page,
        name='products'
    ),
    path(
        'product/',
        views.product,
        name='product'
    ),
    path(
        'promo/',
        views.promo
    ),
    path(
        'contacts/',
        views.contacts
    ),
    path(
        'about/',
        views.about
    ),
    path(
        'dashboard/',
        views.dashboard,
        name="dashboard"
    ),
    path(
        'search/',
        views.search,
        name="search"
    ),
    
    re_path(
        r'^login/$',
        LoginView.as_view(template_name="login.html", authentication_form=LoginForm),
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

    path(
        'db_auto_fill/<int:amount>/<model>/',
        views.db_auto_fill,
        name='db_auto_fill'
    ),
]