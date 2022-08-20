from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Index page
def index(request):
    slider_images = Main_page_slider.objects.all()
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    random_product = Products.objects.order_by('?').first()
    latest_products_per_category = {}
    
    # Get N products per category in dict
    for category in categories:
        latest_products_per_category[category] = Products.objects.filter(subcategory__category = category)[:5]
        
    data = {
        "categories": categories, 
        "subcategories": subcategories,
        "slider_images": slider_images,
        "random_product": random_product,
        "latest_products_per_category": latest_products_per_category,
    }

    return render(request, "index.html", context=data)


def products(request, page=1, category=None, subcategory=None):
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    random_product = Products.objects.order_by('?').first()
    
    if request.GET.get('subcategory'):
        subcategory = request.GET['subcategory']
        products = Products.objects.filter(subcategory = subcategory)
    elif request.GET.get('category'):
        category = request.GET['category']
        products = Products.objects.filter(subcategory__category = category)
    else:
        products = Products.objects.all()
    
    paginator = Paginator(products, 12)  # Show 12 products per page
    products = paginator.get_page(request.GET.get("page", 1))
    page_range = paginator.get_elided_page_range(number=1, on_each_side=3, on_ends=2)
    
    data = {
        "categories": categories,
        "subcategories": subcategories,
        "products": products,
        "random_product": random_product,
        "page_range": page_range,
    }
    
    return render(request, "shop_page.html", context=data)

def contacts(request):
    categories = Categories.objects.all()
    slider_images = Main_page_slider.objects.all()
    
    data = {"categories": categories, "slider_images": slider_images}
    
    return render(request, "about.html", context=data)

def promo(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

# Registration page
def registration(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():

            # Create a new user object but avoid saving it yet
            new_user = registration_form.save(commit=False)

            # Set email like username
            new_user.username = (registration_form.cleaned_data['email'])

            # Set the chosen password
            new_user.set_password(registration_form.cleaned_data['password1'])

            # Save the User object
            new_user.save()
            return render(request, "registration_done.html", {"new_user": new_user})
        else:
            registration_form = RegistrationForm(request.POST)
            return render(request, "registration.html", {"registration_form": registration_form})

    else:
        registration_form = RegistrationForm()
        return render(request, "registration.html", {"registration_form": registration_form})

# Dashboard page
@login_required
def dashboard(request):
    return render(request, "dashboard.html", {'section': 'dashboard'})