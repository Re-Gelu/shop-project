from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)
    required_css_class = "uk-search-input"

class Submit_order(forms.Form):
    email = forms.EmailField(max_length=40, required=True)
    adress = forms.CharField(max_length=100, required=True, label="Адрес")
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = forms.CharField(validators = [phoneNumberRegex], max_length = 16, label="Номер телефона")
    #required_css_class = 'form-control'
    
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'
