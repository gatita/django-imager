from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from models import ImagerProfile


@receiver(post_save, sender=User)
def auto_create_profile(sender, **kwargs):
    if kwargs.get('raw'):
        return

    try:
        instance = kwargs['instance']
        instance.profile
    except ImagerProfile.DoesNotExist:
        instance.profile = ImagerProfile()
        instance.profile.save()


@receiver(post_delete, sender=User)
def auto_delete_profile(sender, **kwargs):
    if kwargs.get('raw'):
        return

    try:
        instance = kwargs['instance']
        instance.profile.delete()
    except ImagerProfile.DoesNotExist:
        pass
