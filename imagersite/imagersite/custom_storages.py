from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


# MediaS3BotoStorage = lambda: S3BotoStorage(
#     location=settings.MEDIA_DIRECTORY, querystring_auth=False
# )


# StaticS3BotoStorage = lambda: S3BotoStorage(
#     location=settings.STATIC_DIRECTORY, querystring_auth=False
# )


class StaticRootS3BotoStorage(S3BotoStorage):
    """
    Storage for static files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.STATIC_DIRECTORY
        super(StaticRootS3BotoStorage, self).__init__(*args, **kwargs)


class MediaRootS3BotoStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.MEDIA_DIRECTORY
        super(MediaRootS3BotoStorage, self).__init__(*args, **kwargs)
