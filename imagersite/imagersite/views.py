# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from imager_images.models import Photo


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        photo = Photo.objects.all().filter(
            published='Public').order_by('?').first()
        context['photo'] = photo
        return context
