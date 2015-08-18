# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.core.files.storage import default_storage
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import PermissionDenied
from models import Photo, Album, Face
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_faces(photo):
    import Algorithmia
    import base64
    Algorithmia.apiKey = os.environ.get('ALGORITHMIA_KEY')

    with default_storage.open(photo.img.name, 'rb') as img:
        b64 = base64.b64encode(img.read())

    rectangles = Algorithmia.algo("/ANaimi/FaceDetection/0.1.2").pipe(b64)

    faces = []
    for rect in rectangles:
        face = Face()
        face.photo = photo
        face.name = '?'
        face.x = rect['x']
        face.y = rect['y']
        face.width = rect['width']
        face.height = rect['height']
        face.save()
        faces.append(face)
    print faces


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
    detect = False

    def get_object(self, **kwargs):
        obj = super(PhotoView, self).get_object(**kwargs)
        if obj.published != 'public' and obj.user != self.request.user:
                raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        if self.detect and len(self.object.faces.all()) == 0:
            get_faces(self.object)

        context['faces'] = self.object.faces.all()
        return context


class PhotoCreate(CreateView):
    model = Photo
    template_name = 'photo_form.html'
    fields = ['img', 'title', 'description', 'published']
    success_url = reverse_lazy('images:library')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhotoCreate, self).form_valid(form)


class AlbumCreate(CreateView):
    model = Album
    template_name = 'album_form.html'
    fields = ['title', 'description', 'photos', 'cover']
    success_url = reverse_lazy('images:library')

    def get_form(self):
        form = super(AlbumCreate, self).get_form()
        form.fields['photos'].queryset = Photo.objects.filter(
            user=self.request.user
        )
        form.fields['cover'].queryset = Photo.objects.filter(
            user=self.request.user
        )
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)


class PhotoEdit(UpdateView):
    model = Photo
    fields = ['title', 'description', 'published']
    template_name = 'photo_edit.html'
    success_url = reverse_lazy('images:library')

    def get_object(self, **kwargs):
        obj = super(PhotoEdit, self).get_object(**kwargs)
        if obj.user != self.request.user:
                raise PermissionDenied
        return obj


class AlbumEdit(UpdateView):
    model = Album
    fields = ['title', 'description', 'cover', 'photos', 'published']
    template_name = 'album_edit.html'
    success_url = reverse_lazy('images:library')

    def get_object(self, **kwargs):
        obj = super(AlbumEdit, self).get_object(**kwargs)
        if obj.user != self.request.user:
                raise PermissionDenied
        return obj

    def get_form(self):
        form = super(AlbumEdit, self).get_form()
        form.fields['photos'].queryset = Photo.objects.filter(
            user=self.request.user
        )
        form.fields['cover'].queryset = Photo.objects.filter(
            user=self.request.user
        )
        return form
