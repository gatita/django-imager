# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from .models import ImagerProfile


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control profile_fix'}),
            'first_name': TextInput(attrs={
                'class': 'form-control profile_fix'}),
            'last_name': TextInput(attrs={
                'class': 'form-control profile_fix'}),
            'email': TextInput(attrs={
                'class': 'form-control profile_fix'}),
        }


class ProfileEditForm(ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['website', 'address', 'camera', 'photo_genre']

        widgets = {
            'website': TextInput(attrs={
                'class': 'form-control profile_fix'}),
            'address': TextInput(attrs={
                'class': 'form-control profile_fix'}),
            'camera': TextInput(attrs={
                'class': 'form-control profile_fix'}),
            'photo_genre': TextInput(attrs={
                'class': 'form-control profile_fix'}),
        }
