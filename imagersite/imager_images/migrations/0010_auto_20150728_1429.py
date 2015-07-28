# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='photo_files/%Y-%m-%d'),
        ),
    ]
