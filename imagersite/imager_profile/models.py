from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )
    camera = models.CharField(
        max_length=255,
        help_text='What is the make and model of your camera?'
    )
    address = models.TextField()
    website = models.URLField()
    photo_genre = models.CharField(max_length=255)

    def is_active(self):
        pass

    def __str__(self):
        pass
