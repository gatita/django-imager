# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from .forms import UserEditForm, ProfileEditForm


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
        user_form = UserEditForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileEditForm(
            request.POST,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse('profile:profile'))

        else:
            context = {
                'user_form': user_form.as_p,
                'profile_form': profile_form.as_p
            }

            return render(
                request,
                'profile_edit.html',
                context
            )

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_form': user_form.as_p,
            'profile_form': profile_form.as_p
        }

        return render(
            request,
            'profile_edit.html',
            context
        )
