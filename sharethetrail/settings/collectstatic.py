from environ import Env
from .base import *

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = "django-insecure-8+-j3rwqe6!p4(^q-6254p@r065j(jci(h75$ij$$(u3j6wj&f"
SITE_TYPE = env.str("SITE_TYPE", default="site")

ALLOWED_HOSTS = [
    "*",
]

AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION", default="us-east-2")

STATICFILES_STORAGE = "storages.backends.s3boto3.S3ManifestStaticStorage"
AWS_STORAGE_BUCKET_NAME = env.str("STATIC_BUCKET_NAME", default="sharethetrail-static")
AWS_LOCATION = f'{SITE_TYPE}/'
AWS_DEFAULT_ACL = None

STATIC_S3_REGION = env.str("STATIC_S3_REGION", default=AWS_S3_REGION_NAME)
STATIC_S3_BUCKET = env.str("STATIC_BUCKET_NAME")
STATIC_LOCATION = f'{SITE_TYPE}/'
STATIC_CLOUDFRONT_DOMAIN = env.str("STATIC_CLOUDFRONT_DOMAIN", default="static.sharethetrail.net")
STATIC_URL = f'https://{STATIC_CLOUDFRONT_DOMAIN}/{STATIC_LOCATION}'
STATIC_ACL = None

try:
    from .local import *
except ImportError:
    pass
