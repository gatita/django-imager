# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from models import Photo, Album


class AlbumView(DetailView):
    model = Album
    template_name = 'album_detail.html'
