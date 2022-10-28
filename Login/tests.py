from django.test import TestCase, override_settings
from django.core.management import call_command
from django.conf import settings
from .forms import RegistrationForm

""" @override_settings(CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
})
@override_settings(EXTRA_SETTINGS_CACHE_NAME='default') """
class RegistrationTests(TestCase):
    
    def test_registration_user(self):
        registration_form=RegistrationForm(
            {
                "email": "test@email.com",
                "first_name": "Name",
                "last_name": "Name2",
                "password1": "GoGo1337",
                "password2": "GoGo1337"
            }
        )
        
        new_user = registration_form.save(commit=False)
        new_user.username = (registration_form.cleaned_data['email'])
        new_user.set_password(registration_form.cleaned_data['password1'])
        new_user.save()
        
        self.assertEqual(new_user.username, "test@email.com")
        self.assertEqual(new_user.email, "test@email.com")
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)