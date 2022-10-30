from django import forms
from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field
from crispy_forms.bootstrap import PrependedText, FormActions

class Submit_order(forms.Form):
    email = forms.EmailField(max_length=40, required=True)
    adress = forms.CharField(max_length=500, required=True, label="Адрес")
    phone_number = PhoneNumberField(label="Номер телефона", region="RU")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'email'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': '+76665554433'})
        
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            PrependedText("email", '@'),
            Field("adress"),
            Field("phone_number"),
            css_class='form-row'
        ),
        FormActions(
            HTML('<hr><button class="btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Оформить заказ!</button>'),
            css_class='col-12 text-center mt-0',
        )
    )