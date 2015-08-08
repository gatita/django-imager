from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class StaticS3BotoStorage(S3BotoStorage):
    """
    Storage for static files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.STATIC_DIRECTORY
        super(StaticS3BotoStorage, self).__init__(*args, **kwargs)


class MediaS3BotoStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.MEDIA_DIRECTORY
        super(MediaS3BotoStorage, self).__init__(*args, **kwargs)
