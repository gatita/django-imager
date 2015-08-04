from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import AlbumView, PhotoView, PhotoCreate, PhotoEdit, AlbumEdit

urlpatterns = [
    url(
        r'^library/',
        login_required(
            TemplateView.as_view(template_name='library.html')
        ),
        name='library'
    ),
    url(
        r'^album/(?P<pk>\d+)/$',
        login_required(
            AlbumView.as_view()
        ),
        name='album_detail'
    ),
    url(
        r'^photo/(?P<pk>\d+)/$',
        login_required(
            PhotoView.as_view()
        ),
        name='photo_detail'
    ),
    url(
        r'^photos/add/',
        login_required(
            PhotoCreate.as_view()
        ),
        name='photo_add'
    ),
    url(
        r'^photos/(?P<pk>\d+)/edit$',
        login_required(
            PhotoEdit.as_view()
        ),
        name='photo_edit'
    ),
    url(
        r'^albums/(?P<pk>\d+)/edit$',
        login_required(
            AlbumEdit.as_view(),
        ),
        name='album_edit'
    )
]
