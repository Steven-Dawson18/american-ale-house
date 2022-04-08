"""Test Checkout Views"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Order, Coupon


class TestProfilesViews(TestCase):
    """ Class to test the profiles views """

    def setUp(self):
        """
        Set up test data
        """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com')
        testuser.save()

        Order.objects.create(
            order_number='987654321',
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

        Coupon.objects.create(
            code='TEST_CODE',
            discount="20",
        )

    def test_empty_bag(self):
        """
        Test bag is empty for checkout
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your bag")
