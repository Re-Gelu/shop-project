from django.forms import EmailField, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Row, Column, Field
from crispy_forms.bootstrap import PrependedText, FormActions
from allauth.account.forms import LoginForm as AuthenticationForm

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"] = EmailField(
            widget=TextInput(attrs={"autofocus": True, 'placeholder': 'email'}),
            label="Адрес электронной почты"
        )
        self.fields['password'].widget.attrs.update({'placeholder': ' '})
        
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            PrependedText("login", '@'),
            Field("password"),
            Field("remember", css_class='background-colored border-colored'),
            css_class='form-row'
        ),
        FormActions(
            HTML('<hr><button class="btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Войти</button>'),
            css_class='col-12 text-center mt-0',
        )
    )

class RegistrationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'email'})
        for key in self.fields:
            self.fields[key].required =True
            
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            PrependedText("email", '@'),
            Column('first_name', css_class='form-group col-md-6'),
            Column('last_name', css_class='form-group col-md-6'),
            css_class='form-row m-0'
        ),
        Row(
            Field('password1', css_class='form-group col-md-6'),
            Field('password2', css_class='form-group col-md-6'),
            css_class='form-row m-0'
        ),
        FormActions(
            HTML('<hr><button class="btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Перейти к покупкам!</button>'),
            css_class='col-12 text-center mt-0',
        )
    )
    
class ChangePassword(PasswordChangeForm):
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('old_password', css_class='form-group'),
            Field('new_password1', css_class='form-group'),
            Field('new_password2', css_class='form-group'),
            css_class='form-row'
        ),
        FormActions(
            HTML('<hr><button class="btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Сменить пароль</button>'),
            css_class='col-12 text-center mt-0',
        )
    )