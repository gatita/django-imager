from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.core import mail
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


class RegistrationTestCase(TestCase):
    def setUp(self):
        user = UserFactory()
        user.set_password('longfallboots')
        user.save()

    def test_new_registration(self):
        client = Client()
        username = 'companion_cube'
        email = 'do_not_incinerate@mailinator.com'
        response = client.post(
            '/accounts/register/',
            {
                'username': username,
                'email': email,
                'password1': 'iamsentient',
                'password2': 'iamsentient',
            },
            follow=True,
        )

        user = User.objects.get(username=username)
        self.assertFalse(user.is_active)

        # check redirect page works
        soup = BeautifulSoup(response.content, 'html5lib')
        self.assertTrue(soup.find(
            text="Please check your email to "
            "complete the registration process."
        ))

        # check mail.outbox
        domain = 'example.com'
        link_lead = domain + '/accounts/activate/'
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(domain, mail.outbox[0].body)
        self.assertIn(link_lead, mail.outbox[0].body)
        self.assertIn(email, mail.outbox[0].recipients())

    def test_existing_registration(self):
        client = Client()
        user = User.objects.get(username='testsubject1')
        response = client.post(
            '/accounts/register/',
            {
                'username': user.username,
                'email': user.email,
                'password1': 'longfallboots',
                'password2': 'longfallboots',
            },
            follow=True,
        )
        self.assertIn(
            'A user with that username already exists',
            response.content
        )
