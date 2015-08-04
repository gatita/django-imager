# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        photo_count = self.request.user.photos.count()
        album_count = self.request.user.albums.count()
        context['photo_count'] = photo_count
        context['album_count'] = album_count
        return context


def profile_edit_view(request):
    if request.method == 'POST':
        pass

    else:
        pass
