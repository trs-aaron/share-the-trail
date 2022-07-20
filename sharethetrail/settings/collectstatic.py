from environ import Env
from .base import *

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = "django-insecure-8+-j3rwqe6!p4(^q-6254p@r065j(jci(h75$ij$$(u3j6wj&f"
FIELD_ENCRYPTION_KEY = "fNvUX56CncnrOb3T9I_XwuRgeUjc1bZ9EFPOb4zj2n0="
SITE_TYPE = env.str("SITE_TYPE", default="site")
SITE_VERSION = env.str("SITE_VERSION")

ALLOWED_HOSTS = [
    "*",
]

AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION", default="us-east-2")

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = env.str("STATIC_BUCKET_NAME", default="sharethetrail-static")
AWS_LOCATION = f'{SITE_TYPE}/{SITE_VERSION}/'
AWS_DEFAULT_ACL = None

STATIC_S3_REGION = env.str("STATIC_S3_REGION", default=AWS_S3_REGION_NAME)
STATIC_S3_BUCKET = env.str("STATIC_BUCKET_NAME")
STATIC_LOCATION = f'{SITE_TYPE}/'
STATIC_CLOUDFRONT_DOMAIN = env.str("STATIC_CLOUDFRONT_DOMAIN", default="static.sharethetrail.net")
STATIC_URL = f'/{SITE_TYPE}/'
STATIC_ACL = None

try:
    from .local import *
except ImportError:
    pass
