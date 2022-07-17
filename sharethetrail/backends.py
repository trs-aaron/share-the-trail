from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage, S3ManifestStaticStorage


class MediaStorage(S3Boto3Storage):
    access_key = settings.MEDIA_AWS_ACCESS_KEY_ID
    secret_key = settings.MEDIA_AWS_SECRET_ACCESS_KEY
    bucket_name = settings.MEDIA_S3_BUCKET
    location = settings.MEDIA_LOCATION
    custom_domain = settings.MEDIA_CLOUDFRONT_DOMAIN
    default_acl = settings.MEDIA_ACL
