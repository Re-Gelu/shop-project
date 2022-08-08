from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Почта", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(min_length=4, max_length=30, label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-control"}))

class RegistrationForm(forms.ModelForm): 
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(min_length=4, max_length=30, label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(min_length=4, max_length=30, label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(min_length=2, max_length=30, label="Имя", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(min_length=2, max_length=30, label="Фамилия", widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:         
            raise ValidationError("Пароли не совпадают!")
        else:
            validate_password(cleaned_data.get("password"), user=cleaned_data.get("email"))
            validate_password(cleaned_data.get("password2"), user=cleaned_data.get("email"))
