# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from imager_images.models import Photo


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        photo_count = self.request.user.photos.count()
        album_count = self.request.user.albums.count()
        context['photo_count'] = photo_count
        context['album_count'] = album_count
        return context
