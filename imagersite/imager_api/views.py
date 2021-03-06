from imager_images.models import Photo
from rest_framework import viewsets
from serializers import PhotoSerializer
from django.db.models import Q


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view  a list of their photos
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        qset = super(PhotoViewSet, self).get_queryset()
        public = Q(published='public')
        if self.request.user.is_anonymous():
            qset = qset.filter(public)

        else:
            private = Q(user=self.request.user)
            qset = qset.filter(public | private).distinct()
        return qset

