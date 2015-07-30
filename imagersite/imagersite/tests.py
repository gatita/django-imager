from django.test import TestCase, Client
from bs4 import BeautifulSoup
# import html5lib
# from django.core import mail
from django.contrib.auth.models import User
import factory


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = 'testsubject1'
    first_name = 'Chell'
    last_name = '[REDACTED]'
    email = 'testsubject1@mailinator.com'


class LoginLogoutTestCase(TestCase):
    def setUp(self):
        user = UserFactory()
        user.set_password('longfallboots')
        user.save()

    def test_login(self):
        client = Client()
        response = client.get('/')
        soup = BeautifulSoup(response.content, 'html5lib')
        self.assertTrue(soup.find('a', text='Login'))
        self.assertFalse(soup.find('div', id='logged_in_user'))
        self.assertFalse(soup.find('a', text='Logout'))

        response = client.post(
            '/accounts/login/',
            {'username': 'testsubject1', 'password': 'longfallboots'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='testsubject1')
        soup = BeautifulSoup(response.content, 'html5lib')
        self.assertIn(
            user.username,
            soup.find('div', id='logged_in_user').text
        )
        self.assertFalse(soup.find('div', text='Logout'))

    def test_logout(self):
        client = Client()
        client.login(username='testsubject1', password='longfallboots')
        response = client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html5lib')
        self.assertTrue(soup.find('a', text='Login'))
        self.assertFalse(soup.find('a', text='Logout'))
