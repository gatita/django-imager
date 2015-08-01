from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from views import AlbumView

urlpatterns = [
    url(r'^library/', login_required(TemplateView.as_view(
                                     template_name='library.html'))),
    url(r'^album/(?P<pk>\d+)/$', login_required(
        AlbumView.as_view()), name='album_detail'),
]
