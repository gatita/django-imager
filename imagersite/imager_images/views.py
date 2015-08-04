# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from models import Photo, Album


class AlbumView(DetailView):
    model = Album
    template_name = 'album_detail.html'

    def get_object(self, **kwargs):
        obj = super(AlbumView, self).get_object(**kwargs)
        if obj.published != 'public' and obj.user != self.request.user:
                raise PermissionDenied
        return obj


class PhotoView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'

    def get_object(self, **kwargs):
        obj = super(PhotoView, self).get_object(**kwargs)
        if obj.published != 'public' and obj.user != self.request.user:
                raise PermissionDenied
        return obj
