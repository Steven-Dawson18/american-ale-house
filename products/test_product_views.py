"""Products Tests Models"""
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Category, Product


class TestProductModels(TestCase):
    """
    Testing Category and Product Views
    """
    def setUp(self):
        """
        Create test user, category, product and review
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        product = Product.objects.create(
            name='Test Product Name',
            price='16.99',
            description='Test Description',
            abv='4.0',
        )

    def test_user_count(self):
        """
        Check users are set up
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_url_response(self):
        """
        Test URL response success
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        """
        This tests get all products view
        """
        response = self.client.get('/products/', {
            'search_term': 'test', 'current_categories': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """
        Product details page test
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/',
                                   {'product': product,
                                    'is_product_in_favourites': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_superuser_add_product(self):
        """
        Test superuser can access the add a product page
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_as_non_superuser(self):
        """
        Test non superuser can't access the add a product page
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Sorry, only store owners can do that.")
