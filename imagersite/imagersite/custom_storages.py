from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


StaticS3BotoStorage = lambda: S3BotoStorage(
    location=settings.STATIC_DIRECTORY, querystring_auth=False
)
