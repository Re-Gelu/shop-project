from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.auth.views import *
from .forms import *
from .views import *

class RegistrationTests(TestCase):
    
    def setUp(self):
        self.url = reverse('registration')
        self.response = self.client.get(self.url)
    
    # registration page tests
    def test_registration_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration.html')
        
    def test_registration_form(self):
        form = self.response.context.get('registration_form')
        self.assertIsInstance(form, RegistrationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_registration_page_resolves_RegistrationPageView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            RegistrationPageView.as_view().__name__
        )
        
    def test_registration_page_correct_html(self):
        self.assertContains(self.response, 'Регистрация')
    
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


class LoginTests(TestCase):
    def setUp(self):
        self.url = reverse('login')
        self.response = self.client.get(self.url)
        
    # login page tests
    def test_login_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_login_page_template(self):
        self.assertTemplateUsed(self.response, 'login.html')

    def test_login_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            LoginView.as_view().__name__
        )
        
    def test_login_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, LoginForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    def test_login_page_correct_html(self):
        self.assertContains(self.response, 'Вход')


class LogoutTests(TestCase):
    def setUp(self):
        self.url = reverse('logout')
        self.response = self.client.get(self.url)

    # logout page tests
    def test_logout_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_logout_page_template(self):
        self.assertTemplateUsed(self.response, 'logout.html')

    def test_logout_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            LogoutView.as_view().__name__
        )
    
    def test_logout_page_correct_html(self):
        self.assertContains(self.response, 'Вы успешно вышли из учетной записи.')

class PasswordChangeTests(TestCase):
    username = 'superadmin'
    password ='testpass123'
    
    def setUp(self):
        user = User.objects.create_superuser(self.username, self.password)
        self.client.force_login(user)
        self.url = reverse('password_change')
        self.response = self.client.get(self.url)

    # password_change page tests
    def test_password_change_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_password_change_page_template(self):
        self.assertTemplateUsed(self.response, 'change_password.html')

    def test_password_change_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            PasswordChangeView.as_view().__name__
        )

    def test_password_change_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ChangePassword)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_password_change_page_correct_html(self):
        self.assertContains(self.response, 'Смена пароля')

class PasswordChangeDoneTests(TestCase):
    username = 'superadmin'
    password = 'testpass123'
        
    def setUp(self):
        user = User.objects.create_superuser(self.username, self.password)
        self.client.force_login(user)
        self.url = reverse('password_change_done')
        self.response = self.client.get(self.url)

    # password_change_done page tests
    def test_password_change_done_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_password_change_done_page_template(self):
        self.assertTemplateUsed(self.response, 'change_password_done.html')

    def test_password_change_done_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            PasswordChangeDoneView.as_view().__name__
        )
        
    def test_password_change_done_page_correct_html(self):
        self.assertContains(self.response, 'Пароль успешно изменён!')
