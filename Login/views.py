from django.shortcuts import render

from .forms import RegistrationForm

from Shop.models import *
from Shop.views import CustomTemplateView

class RegistrationPageView(CustomTemplateView):
    """ Registration page class view """
    
    template_name = "registration.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"registration_form": RegistrationForm()})
    
    def post(self, request, *args, **kwargs):
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
            return render(request, self.template_name, {"registration_form": registration_form})
