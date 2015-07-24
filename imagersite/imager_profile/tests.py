from django.test import TestCase
from django.contrib.auth.models import User
import factory
from .models import ImagerProfile


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    email = factory.Sequence(lambda n: 'user{}@mailinator.com'.format(n))


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user0 = UserFactory.build()
        self.user1 = UserFactory.build()
        self.user2 = UserFactory.build()

    def test_profile_created_on_user_save(self):
        self.assertEqual(ImagerProfile.objects.count(), 0)

        self.user0.save()

        self.assertEqual(ImagerProfile.objects.count(), 1)

    def test_profile___str___is_formatted_properly(self):
        self.user0.save()
        profile = ImagerProfile.objects.get(user=self.user0)

        self.assertEqual(
            "{}'s profile".format(self.user0.username),
            str(profile)
        )

    def test_profile_deleted_on_user_delete(self):
        self.user0.save()

        num_profiles = ImagerProfile.objects.count()
        self.user0 = User.objects.all()[0]

        self.user0.delete()

        self.assertEqual(
            num_profiles - 1,
            ImagerProfile.objects.count()
        )

    def test_profile_is_active_method(self):
        self.user0.save()
        self.profile0 = ImagerProfile.objects.all()[0]

        self.assertTrue(self.profile0.is_active)

    def test_profile_is_active_when_user_inactive(self):
        self.user0.is_active = False
        self.user0.save()

        self.profile0 = ImagerProfile.objects.all()[0]

        self.assertFalse(self.profile0.is_active)
