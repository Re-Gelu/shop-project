from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Column, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'

        self.fields["username"].label = "Адрес электронной почты"


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            PrependedText("email", '@'),
            Column('first_name', css_class='form-group col-md-6'),
            Column('last_name', css_class='form-group col-md-6'),
            css_class='form-row'
        ),
        Row(
            Column('password1', css_class='form-group col-md-6'),
            Column('password2', css_class='form-group col-md-6'),
            css_class='form-row'
        ),
        FormActions(
            HTML('<hr><button class="btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Перейти к покупкам!</button>'),
            css_class='col-12 text-center mt-0',
        )
    )
    
class ChangePassword(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'