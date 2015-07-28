# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20150724_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_modified',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
