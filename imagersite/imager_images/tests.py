from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from imager_images.models import Photo, Album
import factory
from faker import Faker


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    username = factory.LazyAttribute(lambda n: 'user{0}'.format(n.first_name))
    email = factory.LazyAttribute(
        lambda n: '{0}@example.com'.format(n.first_name)
    )


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    img = fake.mime_type()
    title = fake.sentence()
    description = fake.sentence()


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    title = fake.sentence()
    description = fake.text()


class PhotoTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()

    def test_create_photo(self):
        assert len(Photo.objects.all()) == 0
        PhotoFactory.create(user=self.user)
        assert len(Photo.objects.all()) == 1

    def test_photo_user_relationship(self):
        test_photo = PhotoFactory.create(user=self.user)
        assert test_photo.user == self.user
        self.assertTrue(
            test_photo.title in
            self.user.photos.first().title
        )

    def test_photo_str_method(self):
        test_photo = PhotoFactory.create(user=self.user)
        self.assertEqual(
            "{} - Photo by {}".format(
                test_photo.title,
                self.user.username
            ),
            str(test_photo)
        )


class AlbumTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.photo = PhotoFactory.create(user=self.user)

    def test_create_album(self):
        self.assertEqual(Album.objects.count(), 0)
        AlbumFactory.create(user=self.user)
        self.assertEqual(Album.objects.count(), 1)

    def test_album_user_relationship(self):
        test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(test_album.user, self.user)

    def test_new_album_contains_no_pictures(self):
        test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(test_album.photos.count(), 0)

    def test_add_photos_to_album(self):
        test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(test_album.photos.count(), 0)
        test_album.photos.add(self.photo)
        self.assertEqual(test_album.photos.count(), 1)

    def test_album_photo_relationship(self):
        test_album = AlbumFactory.create(user=self.user)
        test_album.photos.add(self.photo)
        self.assertEqual(self.photo.albums.first(), test_album)
        self.assertEqual(test_album.photos.first(), self.photo)


class LibraryViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create(username='foo')
        cls.user.set_password('secret')
        cls.user.save()
        cls.photo = PhotoFactory.create(user=cls.user)
        cls.album = AlbumFactory.create(user=cls.user)
        cls.album.photos.add(cls.photo)
        cls.album.save()

    def test_library_view_redirects_anonymous_user(self):
        resp = self.client.get(reverse('images:library'), follow=True)
        self.assertRedirects(resp, '/accounts/login/?next=/images/library/')

    def test_library_view_auth_user(self):
        self.client.login(username='foo', password='secret')
        resp = self.client.get(reverse('images:library'), follow=True)
        self.assertTemplateUsed(resp, 'library.html')
        self.assertContains(resp, 'gallery-item', count=2)


class AlbumViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create(username='foo')
        cls.user.set_password('secret')
        cls.user.save()
        cls.photo = PhotoFactory.create(user=cls.user)
        cls.album = AlbumFactory.create(user=cls.user)
        cls.album.photos.add(cls.photo)
        cls.album.save()
        cls.public_album = AlbumFactory.create(
            user=cls.user, published='public')

    def test_album_view_redirects_anonymous_user(self):
        resp = self.client.get(reverse(
            'images:album_detail',
            kwargs={'pk': self.album.pk}),
            follow=True)
        self.assertRedirects(
            resp,
            '/accounts/login/?next=/images/album/{}/'.format(self.album.pk)
        )

    def test_album_view_auth_user(self):
        self.client.login(username='foo', password='secret')
        resp = self.client.get(reverse(
            'images:album_detail',
            kwargs={'pk': self.album.pk}),
            follow=True)
        self.assertTemplateUsed(resp, 'album_detail.html')
        self.assertContains(resp, 'gallery-item', count=1)

    def test_private_album_view_unauthorized_user(self):
        devious_user = UserFactory.create(username='bar')
        devious_user.set_password('reallysecret')
        devious_user.save()
        self.client.login(username='bar', password='reallysecret')
        resp = self.client.get(reverse(
            'images:album_detail',
            kwargs={'pk': self.album.pk}),
            follow=True)
        self.assertEqual(resp.status_code, 403)

    def test_public_album_non_owner_viewer(self):
        curious_user = UserFactory.create(username='biz')
        curious_user.set_password('baz')
        curious_user.save()
        self.client.login(username='biz', password='baz')
        resp = self.client.get(reverse(
            'images:album_detail',
            kwargs={'pk': self.public_album.pk}),
            follow=True)
        self.assertTemplateUsed(resp, 'album_detail.html')
        self.assertContains(resp, 'gallery')


class PhotoViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create(username='chell')
        cls.user.set_password('longfallboots')
        cls.user.save()
        cls.photo = PhotoFactory.create(user=cls.user)
        cls.album = AlbumFactory.create(user=cls.user)
        cls.album.photos.add(cls.photo)
        cls.album.save()
        cls.public_album = AlbumFactory.create(
            user=cls.user, published='public')
        cls.public_photo = PhotoFactory.create(
            user=cls.user, published='public')

    def test_photo_view_redirects_anonymous_user(self):
        resp = self.client.get(reverse(
            'images:photo_detail',
            kwargs={'pk': self.photo.pk},
        ),
            follow=True)

        self.assertRedirects(
            resp,
            '/accounts/login/?next=/images/photo/{}/'.format(self.photo.pk)
        )

    def test_photo_view_auth_user(self):
        self.client.login(username='chell', password='longfallboots')
        resp = self.client.get(
            reverse(
                'images:photo_detail',
                kwargs={'pk': self.photo.pk}
            ),
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'photo_detail.html')
        self.assertContains(resp, 'photo_detail', count=1)

    def test_private_photo_view_unauthorized_user(self):
        devious_user = UserFactory.create(username='wheatley')
        devious_user.set_password('space')
        devious_user.save()
        self.client.login(username='wheatley', password='space')
        resp = self.client.get(
            reverse(
                'images:photo_detail',
                kwargs={'pk': self.photo.pk}
            ),
            follow=True
        )
        self.assertEqual(resp.status_code, 403)

    def test_public_photo_non_owner_viewer(self):
        curious_user = UserFactory.create(username='turret')
        curious_user.set_password('iseeyou')
        curious_user.save()
        self.client.login(username='turret', password='iseeyou')
        resp = self.client.get(
            reverse(
                'images:photo_detail',
                kwargs={'pk': self.public_photo.pk}
            ),
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'photo_detail.html')
        self.assertContains(resp, 'photo_detail', count=1)
