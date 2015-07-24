from django.db import models
from django.contrib.auth.models import User


# @python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )
    camera = models.CharField()
    address = models.TextField()
    website = models.URLField()
    photo_genre = models.CharField()

    def is_active(self):
        pass

    def __str__(self):
        pass
