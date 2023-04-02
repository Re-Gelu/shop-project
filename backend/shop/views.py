from extra_settings.models import Setting
from watson import search as watson
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from django.views.generic.base import TemplateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from cart.cart import Cart
from orders.models import *
from .serializers import *
from .models import *
from .db_auto_fill import db_auto_fill

# ViewSets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ('subcategory', 'subcategory__category')


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
        
        
# Views

@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class CustomTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        context["subcategories"] = Subcategories.objects.all()
        context["random_product"] = Products.objects.order_by('?').first()
        context["cart"] = Cart(self.request)
        return context


@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class IndexPageView(CustomTemplateView):
    """ Index page class view """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get N products per category in dict
        latest_products_per_category = {}
        for category in context["categories"]:
            latest_products_per_category[category] = Products.objects.filter(
                subcategory__category=category)[:10]

        context["slider_images"] = MainPageSlider.objects.all()
        context["latest_products_per_category"] = latest_products_per_category

        return context


@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class ProductsPageView(CustomTemplateView):
    """ Products page class view """

    template_name = "shop_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = kwargs.get("category")
        subcategory = kwargs.get("subcategory")

        # Vars getted from GET or cache (temporary solution)
        page = self.request.GET.get('page', 1)
        search_query = self.request.GET.get(
            'search_query', cache.get('search_query')
        )
        sort_by = self.request.GET.get('sort_by', cache.get('sort_by'))

        # Caching
        cache.set("sort_by", sort_by)

        # Getting and sorting products from DB
        if search_query:
            products = watson.filter(Products, search_query)
        elif subcategory:
            products = Products.objects.filter(subcategory__name=subcategory)
        elif category:
            products = Products.objects.filter(
                subcategory__category__name=category
            )
        else:
            products = Products.objects.all()

        if sort_by:
            match int(sort_by):
                case 1:
                    pass
                case 2:
                    products = products.order_by('price')
                case 3:
                    products = products.order_by('-price')
                case 4:
                    products = products.order_by('price', '-promo_price')

        # Pagination with N products per page
        paginator = Paginator(
            products, 
            Setting.get(
                "PRODUCTS_PER_PAGE", 
                default=12
            )
        )
        products = paginator.get_page(page)

        context["products"] = products
        context["page_range"] = paginator.page_range
        context["category"] = category
        context["subcategory"] = subcategory

        return context
    

@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class ProductPageView(CustomTemplateView):
    """ Product page class view"""

    template_name = "product_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('id'):
            try:
                context["product"] = Products.objects.get(
                    id=int(self.request.GET['id'])
                )
            except ObjectDoesNotExist:
                context["product"] = False

        return context


class DashboardPageView(LoginRequiredMixin, CustomTemplateView):
    """ Dashboard page class view"""

    template_name = "dashboard.html"
    login_url = 'custom_login'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_orders"] = Orders.objects.filter(
            user_id=self.request.user.id
        )
        return context

    def test_cookies(self) -> bool:
        """ Cookies test """

        self.request.session.set_test_cookie()

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        else:
            return False
