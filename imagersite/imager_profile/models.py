# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User


# Use a modified manager instead of writing a class method to return a
# list comprehension; the manager will return a queryset, which is
# lazily-evaluated, which means that it won't be evaluated until the
# last possible moment.
# The list comprehension is not "The Django Way" since it reaches out
# above the class, whereas Django prefers these types of things to be
# single-row operations.
class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProfileManager, self).get_queryset()\
            .filter(user__is_active=True)


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
    active = ActiveProfileManager()

    @property
    def is_active(self):
        return self.user.is_active

    def __str__(self):
        return "{}'s profile".format(self.user.username)
