"""Products Tests Models"""
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product, ReviewRating


class TestProductModels(TestCase):
    """
    Testing Category, Product and ReviewRating models
    """
    def setUp(self):
        """
        Create test user, category, product and review
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        product = Product.objects.create(
            name='Test Product Name',
            price='16.99',
            description='Test Description',
            abv='4.0',
        )
        ReviewRating.objects.create(
            user=test_user,
            product=product,
            rating='5',
            review='Test Review Text',
        )

    def test_string_method_of_category_returns_name(self):
        """
        Test model returns Category name and friendly name as a string
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_string_method_of_product_returns_name(self):
        """
        Test model returns Category name and friendly name as a string
        """
        product = Product.objects.get(name='Test Product Name')
        self.assertEqual((product.__str__()), product.name)
