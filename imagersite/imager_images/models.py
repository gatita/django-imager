from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Album(models.Model):
    user = models.ForeignKey(
        User,
        related_name='albums',
        null=False
    )

    photos = models.ManyToManyField(
        Photo,
        related_name='albums',
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField()
    date_published = models.DateTimeField()
    cover = models.ForeignKey(
        Photo,
        related_name='album_cover')

    def __str__(self):
        return "{}'s album".format(self.user.username)
