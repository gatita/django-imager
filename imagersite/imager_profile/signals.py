from django.contrib.auth.models import User
from django.core.signals import post_save
from django.dispath import receiver


@receiver(post_save, sender=User)
def dummy_receiver(sender, dispatch_uid='unique_identifier', **kwargs):
    pass
