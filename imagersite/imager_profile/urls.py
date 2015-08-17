from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from imager_profile.views import ProfileView, profile_edit_view


urlpatterns = [
    url(
        r'^$',
        login_required(
            ProfileView.as_view()
        ),
        name='profile'
    ),
    url(
        r'^edit/$',
        login_required(
            profile_edit_view,
        ),
        name='profile_edit'
    )
]
