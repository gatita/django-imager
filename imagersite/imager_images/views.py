# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
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


class PhotoCreate(CreateView):
    model = Photo
    template_name = 'photo_form.html'
    fields = ['img', 'title', 'description', 'published']
    success_url = reverse_lazy('images:library')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhotoCreate, self).form_valid(form)
