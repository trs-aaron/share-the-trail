from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    access_key = settings.MEDIA_AWS_ACCESS_KEY_ID
    secret_key = settings.MEDIA_AWS_SECRET_ACCESS_KEY
    bucket_name = settings.MEDIA_S3_BUCKET
    location = settings.MEDIA_LOCATION
    custom_domain = settings.MEDIA_CLOUDFRONT_DOMAIN
    default_acl = settings.MEDIA_ACL


# class StaticStorage(S3ManifestStaticStorage):
#     access_key = settings.STATIC_AWS_ACCESS_KEY_ID
#     secret_key = settings.STATIC_AWS_SECRET_ACCESS_KEY
#     bucket_name = settings.STATIC_S3_BUCKET
#     location = settings.STATIC_LOCATION
#     root = settings.STATIC_ROOT
#     custom_domain = settings.STATIC_CUSTOM_DOMAIN
#     default_acl = settings.STATIC_ACL
