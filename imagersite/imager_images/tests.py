from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
import factory
from faker import Faker


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    username = factory.Sequence(lambda n: 'user{}'.format(n))
    email = factory.Sequence(lambda n: 'user{}@example.com'.format(n))


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    user = 


class PhotoTestCase(TestCase):

    def setUp(self):
        user = UserFactory.build()

    def tearDown(self):
        pass

    def test_