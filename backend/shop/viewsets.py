from django.conf import settings
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from extra_settings.models import Setting
from orders.models import *
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .db_auto_fill import db_auto_fill
from .models import *
from .serializers import *

# Кэшируются только GET и HEAD ответы со статусом 200
default_decorators = (cache_page(getattr(settings, 'CACHING_TIME', 60)), vary_on_headers("Authorization",))

# ViewSets


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
    filterset_fields = {
        'name': ['iexact', 'icontains', ],
        'price': ['gte', 'lte'],
        'promo_price': ['gte', 'lte'],
        'subcategory': ['exact'],
        'subcategory__category': ['exact']
    }


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = None


class SubcategoriesViewSet(viewsets.ModelViewSet):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    pagination_class = None
    filterset_fields = ('category',)


class DBAutoFillViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'model': openapi.Schema(type=openapi.TYPE_STRING, description='Model in DB'),
                'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='Amount to add', default=1),
            }
        ),
        responses={'201': DBAutoFillSerializer}
    )
    def create(self, request):
        serializer = DBAutoFillSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        db_auto_fill(
            int(serializer.validated_data.get("amount")),
            serializer.validated_data.get("model")
        )
        return Response(
            {"message": f'Успешно добавлено {serializer.validated_data.get("amount")} записей в таблицу {serializer.validated_data.get("model")}!'},
            status=status.HTTP_201_CREATED
        )


class MainSettingsViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({
            "SITE_NAME": Setting.get("SITE_NAME"),
            "PRODUCTS_PER_PAGE": Setting.get("PRODUCTS_PER_PAGE"),
            "EMAIL_1": Setting.get("EMAIL_1"),
            "EMAIL_2": Setting.get("EMAIL_2"),
            "PHONE_NUMBER_1": Setting.get("PHONE_NUMBER_1"),
            "PHONE_NUMBER_2": Setting.get("PHONE_NUMBER_2"),
            "LOCATION": Setting.get("LOCATION"),
            "LOCATION_MAP_HTML": Setting.get("LOCATION_MAP_HTML"),
            "ABOUT_PAGE_INFORMATION": Setting.get("ABOUT_PAGE_INFORMATION"),
            "LOCATION_MAP_HTML": Setting.get("LOCATION_MAP_HTML"),
            "LOCATION_MAP_HTML": Setting.get("LOCATION_MAP_HTML"),
        },
            status=status.HTTP_200_OK)


class IndexPageViewSet(viewsets.ViewSet):

    def list(self, request):
        categories = Categories.objects.all()

        # Get N products per category in dict
        queryset = [{
            "id": category.id,
            "name": category.name,
            "subcategories": Subcategories.objects.filter(
                    category=category
                    ),
            "products": ProductsWithAbsoluteURLSerializer(
                Products.objects.filter(
                    subcategory__category=category
                )[:10],
                many=True,
                context={'request': request}
            ).data
        } for category in categories]

        serializer = IndexPageSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
