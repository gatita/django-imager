# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0007_auto_20150724_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='album_cover', to='imager_images.Photo', null=True),
        ),
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
