from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


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

    objects = models.Manager()

    @classmethod
    def active(cls):
        return [profile for profile in cls.objects.all()
                if profile.user.is_active]

    def __str__(self):
        return "{}'s profile".format(self.user.username)


@receiver(post_save, sender=User)
def auto_create_profile(sender, instance, **kwargs):
    try:
        instance.profile
    except ImagerProfile.DoesNotExist:
        instance.profile = ImagerProfile()
        instance.profile.save()


@receiver(post_delete, sender=User)
def auto_delete_profile(sender, instance, **kwargs):
    try:
        instance.profile.delete()
    except ImagerProfile.DoesNotExist:
        pass
