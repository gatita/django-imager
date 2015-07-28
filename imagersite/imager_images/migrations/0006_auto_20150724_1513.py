# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0005_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(related_name='photo', to=settings.AUTH_USER_MODEL),
        ),
    ]
