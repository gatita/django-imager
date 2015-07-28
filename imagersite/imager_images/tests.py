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
        self.test_photo = PhotoFactory.create(user=self.user)
        assert len(Photo.objects.all()) == 1

    def test_photo_user_relationship(self):
        self.test_photo = PhotoFactory.create(user=self.user)
        assert self.test_photo.user == self.user
        self.assertTrue(
            self.test_photo.title in
            self.user.photos.first().title
        )

    def test_photo_str_method(self):
        self.test_photo = PhotoFactory.create(user=self.user)
        self.assertEqual(
            "{} - Photo by {}".format(
                self.test_photo.title,
                self.user.username
            ),
            str(self.test_photo)
        )


class AlbumTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.photo = PhotoFactory.create(user=self.user)

    def test_create_album(self):
        self.assertEqual(Album.objects.count(), 0)
        self.test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(Album.objects.count(), 1)

    def test_album_user_relationship(self):
        self.test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(self.test_album.user, self.user)

    def test_new_album_contains_no_pictures(self):
        self.test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(self.test_album.photos.count(), 0)

    def test_add_photos_to_album(self):
        self.test_album = AlbumFactory.create(user=self.user)
        self.assertEqual(self.test_album.photos.count(), 0)
        self.test_album.photos.add(self.photo)
        self.assertEqual(self.test_album.photos.count(), 1)

    def test_album_photo_relationship(self):
        self.test_album = AlbumFactory.create(user=self.user)
        self.test_album.photos.add(self.photo)
        self.assertEqual(self.photo.albums.first(), self.test_album)
        self.assertEqual(self.test_album.photos.first(), self.photo)
