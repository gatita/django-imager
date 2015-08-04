# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0010_auto_20150728_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='published',
            field=models.CharField(default='private', max_length=255, choices=[('public', 'public'), ('shared', 'shared'), ('private', 'private')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 22, 15, 35, 492355, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 22, 15, 42, 61686, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(default='private', max_length=255, choices=[('public', 'public'), ('shared', 'shared'), ('private', 'private')]),
        ),
    ]
