from django.shortcuts import render
from .forms import RegistrationForm
from Shop.models import *
from Cart.cart import Cart
from Cart.forms import *
# Create your views here.

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

        context = {
            "registration_form": registration_form
        }

        context.update(get_base_context_data(request))

        return render(request, "registration.html", context=context)