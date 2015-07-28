# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imager_images', '0004_auto_20150724_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField()),
                ('date_published', models.DateTimeField()),
                ('cover', models.ForeignKey(related_name='album_cover', to='imager_images.Photo')),
                ('photos', models.ManyToManyField(related_name='albums', to='imager_images.Photo')),
                ('user', models.ForeignKey(related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
