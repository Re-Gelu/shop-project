from ctypes import sizeof
from django.shortcuts import render
from .models import *

def index(request):
    slider_images = Main_page_slider.objects.all()
    categories = Categories.objects.all()
    products = Products.objects.all()
    data = {
        "categories": categories, 
        "slider_images": slider_images,
        "products" : products,
        }

    return render(request, "index.html", context=data)

def contacts(request):
    categories = Categories.objects.all()
    slider_images = Main_page_slider.objects.all()
    data = {"categories": categories, "slider_images": slider_images}
    
    return render(request, "about.html", context=data)

def promo(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

# Create your views here.
