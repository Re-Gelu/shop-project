from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import *
from .models import *

class IndexViewTests(TestCase):
    
    def setUp(self):
        self.url = reverse('index')
        self.response = self.client.get(self.url)
    
    # Index page tests
    def test_index_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'index.html')
        
    def test_index_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
    
    def test_index_page_resolves_IndexPageView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            IndexPageView.as_view().__name__
        )
        
class ProductsViewTests(TestCase):
    
    def setUp(self):
        self.url = reverse('products')
        self.response = self.client.get(self.url)
        
    # Products page tests
    def test_products_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        response = self.client.get('/products/?sort_by=1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/products/?search_query=test')
        self.assertEqual(response.status_code, 200)

    def test_products_page_template(self):
        self.assertTemplateUsed(self.response, 'shop_page.html')
        
    def test_products_page_resolves_ProductsPageView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            ProductsPageView.as_view().__name__
        )

class ProductViewTests(TestCase):
    
    def setUp(self):
        self.url = reverse('product')
        self.response = self.client.get(self.url)
    
    # Product page tests
    def test_product_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        response = self.client.get('/product/?id=1')
        self.assertEqual(response.status_code, 200)
    
    def test_products_page_template(self):
        self.assertTemplateUsed(self.response, 'product_page.html')

    def test_product_page_resolves_ProductPageView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            ProductPageView.as_view().__name__
        )

class ContactsViewTests(TestCase):
    
    def setUp(self):
        self.url = reverse('contacts')
        self.response = self.client.get(self.url)
    
    # Contacts page tests
    def test_contacts_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contacts_page_template(self):
        self.assertTemplateUsed(self.response, 'contacts.html')

    def test_contacts_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            CustomTemplateView.as_view().__name__
        )

class AboutViewTests(TestCase):

    def setUp(self):
        self.url = reverse('about')
        self.response = self.client.get(self.url)
        
    # About page tests
    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            CustomTemplateView.as_view().__name__
        )

class DeliveryViewTests(TestCase):

    def setUp(self):
        self.url = reverse('delivery')
        self.response = self.client.get(self.url)
        
    # Delivery page tests
    def test_delivery_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_delivery_page_template(self):
        self.assertTemplateUsed(self.response, 'delivery.html')

    def test_delivery_page_resolves_CustomTemplateView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            CustomTemplateView.as_view().__name__
        )

class DashboardViewTests(TestCase):
    username = 'superadmin'
    password = 'testpass123'

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser('superadmin', 'superadmin@email.com', 'testpass123')

    def setUp(self):
        self.client.login(username=self.username, password=self.password)
        self.url = reverse('dashboard')
        self.response = self.client.get(self.url)
        
    # Dashboard page tests
    def test_dashboard_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_dashboard_page_template(self):
        self.assertTemplateUsed(self.response, 'dashboard.html')

    def test_dashboard_page_resolves_DashboardPageView(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            DashboardPageView.as_view().__name__
        )
class db_auto_fillViewTests(TestCase):
    username = 'superadmin'
    password = 'testpass123'

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser('superadmin', 'superadmin@email.com', 'testpass123')

    def setUp(self):
        self.client.login(username=self.username, password=self.password)
        self.db_auto_fill_response_1 = self.client.get('/db_auto_fill/3/Categories/')
        self.db_auto_fill_response_2 = self.client.get('/db_auto_fill/10/Subcategories/')
        self.db_auto_fill_response_3 = self.client.get('/db_auto_fill/50/Products/')
        
    # db_auto_fill page tests
    def test_db_auto_fill_status_code(self):
        self.assertEqual(self.db_auto_fill_response_1.status_code, 200)
        self.assertEqual(self.db_auto_fill_response_2.status_code, 200)
        self.assertEqual(self.db_auto_fill_response_3.status_code, 200)

    def test_db_auto_fill_contains_correct_html(self):
        self.assertContains(self.db_auto_fill_response_1, 'Успешно добавлено 3 записей в таблицу Categories!')
        self.assertContains(self.db_auto_fill_response_2, 'Успешно добавлено 10 записей в таблицу Subcategories!')
        self.assertContains(self.db_auto_fill_response_3, 'Успешно добавлено 50 записей в таблицу Products!')
        
class ProductsModelTests(TestCase):
    def setUp(self):
        self.product = Products.objects.create(
            name='test product',
            price=200,
            promo_price=250,
            stock=100,
            available=True
        )
    
    def test_product_listing(self):
        self.assertEqual(self.product.name, 'test product')
        self.assertEqual(self.product.price, 200)
        self.assertIsNone(self.product.promo_price)
        self.assertEqual(self.product.stock, 100)
        self.assertTrue(self.product.available)

    def test_product_view(self):
        response = self.client.get('/product/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test product')
        self.assertTemplateUsed(response, 'product_page.html')
        
class CategoriesModelTests(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            name='test category'
        )
    
    def test_category_listing(self):
        self.assertEqual(self.category.name, 'test category')
        
    def test_category_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test category')
        self.assertTemplateUsed(response, 'index.html')


class SubcategoriesModelTests(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            name='test category'
        )
        self.subcategory = Subcategories.objects.create(
            name='test subcategory',
            category=self.category
        )
        
    def test_subcategory_listing(self):
        self.assertEqual(self.subcategory.name, 'test subcategory')
        
    def test_subcategory_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test subcategory')
        self.assertTemplateUsed(response, 'index.html')
