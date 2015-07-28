# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Photo(models.Model):
    user = models.ForeignKey(
        User,
        related_name='photos',
        null=False
    )

    img = models.ImageField(blank=True)

    title = models.CharField(max_length=255)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    date_published = models.DateTimeField(null=True, blank=True)

    published = models.CharField(max_length=15)

    objects = models.Manager()

    def __str__(self):
        return "Photo owned by {}".format(self.user.username)


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
    date_modified = models.DateTimeField(null=True, blank=True)
    date_published = models.DateTimeField(null=True, blank=True)

    cover = models.ForeignKey(
        Photo,
        related_name='album_cover',
        null=True)

    objects = models.Manager()

    def __str__(self):
        return "{}'s {} album".format(self.user.username, self.title)
