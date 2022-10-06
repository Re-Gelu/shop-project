from django import forms
from phonenumber_field.formfields import PhoneNumberField

class Submit_order(forms.Form):
    email = forms.EmailField(max_length=40, required=True)
    adress = forms.CharField(max_length=500, required=True, label="Адрес")
    phone_number = PhoneNumberField(label="Номер телефона", region="RU")

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'