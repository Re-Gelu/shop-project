from django import forms

class Cart_add_one_product_form(forms.Form):
    product_add_or_remove_one = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)
    
class Cart_remove_one_product_form(forms.Form):
    product_add_or_remove_one = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)