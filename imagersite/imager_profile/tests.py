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

    def test_profile_str_is_formatted_properly(self):
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

    def test_profile_is_active_property(self):
        self.user0.save()
        self.profile0 = ImagerProfile.objects.all()[0]

        self.assertTrue(self.profile0.is_active)

    def test_profile_is_active_property_when_user_inactive(self):
        self.user0.is_active = False
        self.user0.save()

        self.profile0 = ImagerProfile.objects.all()[0]

        self.assertFalse(self.profile0.is_active)

    def test_profile_active_classmethod(self):
        usrs = [self.user0, self.user1, self.user2]

        for i, each in enumerate(usrs):
            each.save()
            each = User.objects.all()[i]

        active_list = ImagerProfile.active.all()

        for each in usrs:
            self.assertTrue(each.profile in active_list)

    def test_profile_active_classmethod_with_inactive_users(self):
        usrs = [self.user0, self.user1, self.user2]

        for i, each in enumerate(usrs):

            if i % 2 != 0:
                each.is_active = False

            each.save()
            each = User.objects.all()[i]

        active_list = ImagerProfile.active.all()

        for each in usrs:
            if each == self.user1:
                self.assertFalse(each.profile in active_list)
            else:
                self.assertTrue(each.profile in active_list)
