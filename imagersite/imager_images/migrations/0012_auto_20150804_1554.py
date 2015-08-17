# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0011_auto_20150728_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
