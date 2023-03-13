"""config URL Configuration

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
from shop.views import *
from cart.views import *
from orders.views import *
from rest_framework import routers
from baton.autodiscover import admin
from django.contrib.auth.views import *
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import mimetypes
import debug_toolbar

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API snippets",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(url="https://github.com/Re-Gelu"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# REST API router
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'subcategories', SubcategoriesViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'db_auto_fill', DBAutoFillViewSet, basename='db_auto_fill')
router.register(r'main_settings', MainSettingsViewSet, basename='main_settings')
router.register(r'index_page', IndexPageViewSet, basename='api_index_page')

urlpatterns = [

    # Filebrowser URLS
    path('admin/filebrowser/', site.urls),

    # TinyMCE URLS
    path('tinymce/', include('tinymce.urls')),

    # Admin app URLS
    path('admin/', admin.site.urls),

    # Baton admin URLS
    path('baton/', include('baton.urls')),

    # Swagger URLS
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    
    # DRF URLS
    path('api/', include(router.urls)),
    
    # Auth URLS
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('api/auth/', include('djoser.urls')),
    
    path('auth/', include('djoser.urls.authtoken')),
    
    # Shop app URLS
    path('', include('shop.urls')),
    
    # Login app URLS
    path('', include('login.urls')),
    
    # Orders app URLS
    path('', include('orders.urls')),
    
    # Cart app URLS
    path('', include('cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
    mimetypes.add_type("application/javascript", ".js", True)