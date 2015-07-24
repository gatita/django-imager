from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# @python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )
    camera = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField()
    photo_genre = models.CharField(max_length=255)

    objects = models.Manager()

    def is_active(self):
        pass

    def __str__(self):
        return "{}'s profile".format(self.user.username)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    try:
        instance.profile
    except ImagerProfile.DoesNotExist:
        instance.profile = ImagerProfile()
        instance.profile.save()
