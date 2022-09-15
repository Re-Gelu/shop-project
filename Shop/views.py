from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST

from .db_auto_fill import DB_AUTO_FILL
from .models import *
from .forms import *

from Cart.cart import Cart
from Cart.forms import *

# Get base context values
def get_base_context_data(request):
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    random_product = Products.objects.order_by('?').first()
    cart_remove_one_form = Cart_remove_one_product_form()
    cart_add_one_form = Cart_add_one_product_form()
    cart = Cart(request)

    base_context = {
        "categories": categories,
        "subcategories": subcategories,
        "random_product": random_product,
        "cart_add_one_form": cart_add_one_form,
        "cart_remove_one_form": cart_remove_one_form,
        "cart": cart
    }
    
    return base_context
        
# Index page
def index(request):
    slider_images = Main_page_slider.objects.all()
    latest_products_per_category = {}
    
    #Cart(request).clear()
    
    # Get N products per category in dict
    for category in get_base_context_data(request)["categories"]:
        latest_products_per_category[category] = Products.objects.filter(subcategory__category = category)[:10]
        
    context = {
        "slider_images": slider_images,
        "latest_products_per_category": latest_products_per_category,
    }
    
    context.update(get_base_context_data(request))

    return render(request, "index.html", context=context)


def products_page(request, page=1, search_query=False):
    if search_query:
        products = search_query
    elif request.GET.get('subcategory'):
        subcategory = request.GET['subcategory']
        products = Products.objects.filter(subcategory__name = subcategory)
    elif request.GET.get('category'):
        category = request.GET['category']
        products = Products.objects.filter(subcategory__category__name = category)
    else:
        products = Products.objects.all()
        
    if request.POST.get('sort_by'):
        match int(request.POST['sort_by']):
            case 1:
                pass
            case 2:
                products = products.order_by('price')
            case 3:
                products = products.order_by('-price')
            case 4:
                products = products.order_by('price', '-promo_price')
    
    paginator = Paginator(products, 12)  # Show N products per page
    products = paginator.get_page(page)
    #page_range = paginator.get_elided_page_range(on_each_side=2, on_ends=1)
    page_range = paginator.page_range
    
    context = {
        "products": products,
        "page_range": page_range,
    }
    
    context.update(get_base_context_data(request))

    return render(request, "shop_page.html", context=context)

def product(request):
    if request.GET.get('id'):
        try:
            product = Products.objects.get(id=int(request.GET['id']))
        except ObjectDoesNotExist:
            product = False
    
    context = {
        "product": product,
    }

    context.update(get_base_context_data(request))
    
    return render(request, "product_page.html", context=context)
def promo(request):
    return render(request, "base.html", context=get_base_context_data(request))

def contacts(request):
    return render(request, "contacts.html", context=get_base_context_data(request))

def delivery(request):
    return render(request, "delivery.html", context=get_base_context_data(request))

def about(request):
    return render(request, "about.html", context=get_base_context_data(request))

# Auto DB fill
@staff_member_required
def db_auto_fill(request, amount, model):
    
    DB_AUTO_FILL(int(amount), model)
    
    return HttpResponse(f'Успешно добавлено {amount} записей в таблицу {model}!')

@require_POST
def search(request):
    if request.POST.get('search_query'):
        search_query = request.POST['search_query']
        products = Products.objects.filter(name__icontains=search_query)

        return products_page(request, 1, products)

# Dashboard page
@login_required
def dashboard(request):
    
    # Cookies test
    print('\n')
    request.session.set_test_cookie()
    print('Cookies - ', request.session.test_cookie_worked())
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    
    # Get cart data
    print('\n')
    for item in get_base_context_data(request)['cart']:
        print(item)
    print('\n')
    
    return render(request, "dashboard.html", context=get_base_context_data(request))