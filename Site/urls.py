"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import *
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from Shop import views
from Shop.forms import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('promo/', views.promo),
    path('contacts/', views.contacts),
    path('about/', views.about),
    path('dashboard/', views.dashboard, name="dashboard"),
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
        PasswordChangeView.as_view(template_name="change_password.html", form_class=ChangePassword), 
        name='password_change'
    ),
    re_path(
        r'^password_change_done/$',
        PasswordChangeDoneView.as_view(template_name="change_password_done.html"), 
        name="password_change_done"
    ),
    
    #re_path(r'^login/$', views.user_login, name='login'),
    #re_path(r'^logout/$', views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
