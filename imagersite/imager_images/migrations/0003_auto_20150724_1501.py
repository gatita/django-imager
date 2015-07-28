# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_photo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_published',
            field=models.DateTimeField(blank=True),
        ),
    ]
