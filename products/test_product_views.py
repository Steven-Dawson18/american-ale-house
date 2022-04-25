"""Products Tests Models"""
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Category, Product, ReviewRating


class TestProductModels(TestCase):
    """
    Testing Category and Product Views
    """
    def setUp(self):
        """
        Create test user, category, product and review
        """
        User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        Product.objects.create(
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

    def test_superuser_can_add_product(self):
        """
        Test superuser can access the add a product page
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_non_superuser_can_not_add_product(self):
        """
        Test non superuser can't access the add a product page
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Sorry, only store owners can do that.")
        self.assertEqual(response.status_code, 302)

    def test_superuser_can_delete_product(self):
        """
        Tests a superuser can delete a product
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Product deleted!")
        deleted_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(deleted_product), 0)

    def test_non_superuser_can_not_delete_product(self):
        """
        Tests a non superuser can't delete a product
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, "
                                           "only store owners can do that.")
        self.assertEqual(response.status_code, 302)

    def test_review_product(self):
        """
        Test a logged in user can add a review to a product
        """
        test_user = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()

        ReviewRating.objects.create(
            user=test_user,
            product=product,
            subject='Test review',
            rating='5',
            review='Test Review Text',
        )
        response = self.client.post(f'/products/submit_review/{product.id}/',
                                    {'subject': 'Test review',
                                     'rating': '5',
                                     'review': 'Test Review Text'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Your review has been successfully added!")

    def test_update_review(self):
        """
        Test a logged in user can update a review on a product
        """
        test_user = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()

        ReviewRating.objects.create(
            user=test_user,
            product=product,
            subject='Test review',
            rating='5',
            review='Test Review Text',
        )
        response = self.client.post('/products/')
        self.assertEqual(response.status_code, 200)

    def test_delete_review(self):
        """
        Test a logged in user can delete a review on a product
        """
        test_user = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()

        ReviewRating.objects.create(
            user=test_user,
            product=product,
            subject='Test review',
            rating='5',
            review='Test Review Text',
        )
        response = self.client.post('/products/')
        self.assertEqual(response.status_code, 200)
