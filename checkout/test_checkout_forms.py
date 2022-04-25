"""
Testing checkout forms
"""

from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test the order form validators
    """

    def test_full_name_required(self):
        """
        Test if form submits without full_name field
        """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_required(self):
        """
        Test form does not submit without email field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'GB',
        })
        # Form should not be valid - email is required
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_required(self):
        """
        Test form does not submit without phone_number
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_is_required(self):
        """
        Test form does not submit without country field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_town_or_city_required(self):
        """
        Test form does not submit without town_or_city field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'country': 'GB',
            'town_or_city': '',
            'street_address1': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address_required(self):
        """
        Test form does not submit without street_address field
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': '',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')
