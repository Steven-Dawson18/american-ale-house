"""Test Checkout Models"""
from django.test import TestCase
from django.contrib.auth.models import User
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

    def test_order_str_method(self):
        """
        This test tests the order number string
        """
        order = Order.objects.get(email='test@test.com')
        self.assertEqual(str(order), order.order_number)

    def test_coupon_str_method(self):
        """
        This test tests the Coupon code
        """
        coupon = Coupon.objects.get()
        self.assertEqual(str('TEST_CODE'), coupon.code)
