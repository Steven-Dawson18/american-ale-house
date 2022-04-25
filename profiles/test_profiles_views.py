from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from checkout.models import Order
from profiles.models import UserProfile


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
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def test_url_response(self):
        """
        Test logged in user can access their profile page
        """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get('/profile/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        """
        Test using correct template in profile page
        """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_order_detail_page(self):
        """
        Test user can see their order history
        """
        self.client.login(username='test_user1', password='test_password')
        test_user = User.objects.get(username='test_user')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get('/profile/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'This is a past confirmation for '
                         'order number 987654321. ' +
                         'A confirmation email was sent on the order date.')

    def test_default_delivery_information_updates(self):
        """
        Test that default delivery info updates
        """
        self.client.login(username='test_user',
                          password='test_password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

        new_data = {
            'default_phone_number': 'testEdit',
            'default_street_address1': 'testEdit',
            'default_town_or_city': 'testEdit',
            'default_postcode': 'testEdit',
            'default_county': 'testEdit',
            'default_country': 'GB'
        }
        self.client.post('/profile/', new_data)
        response = self.client.post('/profile/', new_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Profile updated successfully')
        self.client.logout()
