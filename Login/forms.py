from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'

        self.fields["username"].label = "Адрес электронной почты"


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class ChangePassword(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'
