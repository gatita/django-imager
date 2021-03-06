# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('public', 'public'),
    ('shared', 'shared'),
    ('private', 'private'),
)


@python_2_unicode_compatible
class Photo(models.Model):
    user = models.ForeignKey(
        User,
        related_name='photos',
        null=False
    )
    img = models.ImageField(upload_to="photo_files/%Y-%m-%d")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)
    published = models.CharField(
        max_length=255,
        choices=CHOICES,
        default='private'
    )

    def __str__(self):
        return "{} - Photo by {}".format(self.title, self.user.username)


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
        blank=True
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)

    cover = models.ForeignKey(
        Photo,
        related_name='album_cover',
        null=True,
        blank=True
    )

    published = models.CharField(
        max_length=255,
        choices=CHOICES,
        default='private'
    )

    def __str__(self):
        return "{} - Album by {}".format(self.title, self.user.username)


@python_2_unicode_compatible
class Face(models.Model):
    photo = models.ForeignKey(
        Photo,
        related_name='faces',
        null=False
    )
    name = models.CharField(max_length=255)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return "Face: {}: {}".format(self.photo.title, self.name)
