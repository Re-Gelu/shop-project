from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from .views import *

class RegistrationTests(TestCase):
    
    def setUp(self):
        url = reverse('registration')
        self.response = self.client.get(url)
    
    # registration page tests
    def test_registration_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration.html')
        
    def test_registration_form(self):
        form = self.response.context.get('registration_form')
        self.assertIsInstance(form, RegistrationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_registration_page_resolves_RegistrationPageView(self):
        view = resolve('/registration/')
        self.assertEqual(
            view.func.__name__,
            RegistrationPageView.as_view().__name__
        )
    
    def test_registration_user(self):
        registration_form=RegistrationForm(
            {
                "email": "test@email.com",
                "first_name": "Name",
                "last_name": "Name2",
                "password1": "testpass123",
                "password2": "testpass123"
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
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
