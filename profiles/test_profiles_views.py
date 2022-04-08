from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestProfilesViews(TestCase):
    """ Class to test the profiles views """

    def setUp(self):
        """
        Set up test data
        """
        self.client = Client()
        self.test_user = User.objects.create_user(
                        username='test_user',
                        email="user@alh.com",
                        password='test_password')

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
        """ Test using correct template """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'profiles/profile.html')
