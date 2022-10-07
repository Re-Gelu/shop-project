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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

urlpatterns = [
    
    # Filebrowser URLS
    path(
        'admin/filebrowser/',
        site.urls
    ),
    
    # TinyMCE URLS
    path(
        'tinymce/', 
        include('tinymce.urls')
    ),
    
    # Payments URLS
    path(
        'payments/', 
        include('payments.urls')
    ),
    
    # Admin app URLS
    path(
        'admin/', 
        admin.site.urls
    ),
    
    # Shop app URLS
    path(
        '', 
        include('Shop.urls')
    ),
    
    # Cart app URLS
    path(
        '',
        include('Cart.urls')
    ),
    
    # Login app URLS
    path(
        '', 
        include('Login.urls')
    ),
    
    # Orders app URLS
    path(
        '', 
        include('Orders.urls')
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)