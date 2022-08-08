from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Index page
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

# Login
""" def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "dashboard.html")
                else:
                    return HTTPResponse('Неверные данные для входа!')
            else:
                return HTTPResponse('Invalid login')

    else:
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form}) """

# Registration
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

# Dashboard
@login_required
def dashboard(request):
    return render(request, "dashboard.html", {'section': 'dashboard'})


# Create your views here.
