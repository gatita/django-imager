# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import ImagerProfile


class UserEditForm(ModelForm):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']


class ProfileEditForm(ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['website', 'address', 'camera', 'photo_genre']
