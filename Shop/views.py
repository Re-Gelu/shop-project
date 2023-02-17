from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from extra_settings.models import Setting
from django.views.generic.base import TemplateView, View
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from watson import search as watson

from .db_auto_fill import db_auto_fill
from .models import *
from .forms import *

from orders.models import *

from cart.cart import cart


@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class CustomTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        context["subcategories"] = Subcategories.objects.all()
        context["random_product"] = Products.objects.order_by('?').first()
        context["cart"] = cart(self.request)
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
            latest_products_per_category[category] = Products.objects.filter(subcategory__category = category)[:10]
            
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
        search_query = self.request.GET.get('search_query', cache.get('search_query'))
        sort_by = self.request.GET.get('sort_by', cache.get('sort_by'))
        
        # Caching
        cache.set("sort_by", sort_by)
        
        # Getting and sorting products from DB
        if search_query:
            products = watson.filter(Products, search_query)
        elif subcategory:
            products = Products.objects.filter(subcategory__name=subcategory)
        elif category:
            products = Products.objects.filter(subcategory__category__name=category)
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
        paginator = Paginator(products, Setting.get("PRODUCTS_PER_PAGE", default=12))
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
                context["product"] = Products.objects.get(id=int(self.request.GET['id']))
            except ObjectDoesNotExist:
                context["product"] = False
                
        return context
    
#@method_decorator(cache_page(settings.CACHING_TIME), name="dispatch")
class DashboardPageView(LoginRequiredMixin, CustomTemplateView):
    """ Dashboard page class view"""
    
    template_name = "dashboard.html"
    login_url = 'login'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_orders"] = orders.objects.filter(user_id=self.request.user.id)
        return context
    
    def test_cookies(self) -> bool:
        """ Cookies test """
        
        self.request.session.set_test_cookie()
        
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        else:
            return False
    
class DB_AutoFillView(PermissionRequiredMixin, View):
    """ Auto DB fill class view """
    
    permission_required = 'is_staff'

    def get(self, request, *args, **kwargs):
        db_auto_fill(int(kwargs["amount"]), kwargs["model"])
        return HttpResponse(
            f"""
                <center><h3>Успешно добавлено {kwargs["amount"]} записей в таблицу {kwargs["model"]}!</h3></center>
                <hr>
                <center><small>with love from Re;Gelu :3</small></center>
            """
        )
