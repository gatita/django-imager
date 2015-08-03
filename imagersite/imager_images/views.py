# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from models import Photo, Album


class AlbumView(DetailView):
    model = Album
    template_name = 'album_detail.html'


class PhotoView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'
