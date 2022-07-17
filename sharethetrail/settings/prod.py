from environ import Env
from .base import *

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = env.str("SECRET_KEY")
SITE_TYPE = env.str("SITE_TYPE", default="site")
SITE_ID = env.str("SITE_ID", default="test")
SITE_VERSION = env.str("SITE_VERSION")
ADMIN_HOST = env.str("ADMIN_HOST", default="sharethetrail.net")
WAGTAIL_SITE_NAME = SITE_ID

ALLOWED_HOSTS = [
    "3.137.207.202",
    "sharethetrail.net",
    ".sharethetrail.net",
    "sharethetrail.democrat",
    ".sharethetrail.democrat",
    "sharethetrail.republican",
    ".sharethetrail.republican",
    "sharethetrail.run",
    ".sharethetrail.run",
    "*",
]

CSRF_TRUSTED_ORIGINS = [
    f'https://{ADMIN_HOST}'
]

INSTALLED_APPS = INSTALLED_APPS + [
    "wagtailcache",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": SITE_ID,
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env.int("DB_PORT", 5432),
    }
}

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_REGION_NAME = env("AWS_S3_REGION", default="us-east-2")

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = env.str("STATIC_BUCKET_NAME", default="sharethetrail-static")
AWS_LOCATION = f'{SITE_TYPE}/{SITE_VERSION}/'
AWS_S3_CUSTOM_DOMAIN = env.str("STATIC_CLOUDFRONT_DOMAIN", default="static.sharethetrail.net")
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}'
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = "sharethetrail.backends.MediaStorage"
MEDIA_S3_REGION = env("MEDIA_S3_REGION", default=AWS_S3_REGION_NAME)
MEDIA_S3_BUCKET = env("MEDIA_BUCKET_NAME")
MEDIA_LOCATION = f'{SITE_ID}/media/'
MEDIA_CLOUDFRONT_DOMAIN = env.str("MEDIA_CDN_DOMAIN", default="media.sharethetrail.net")
MEDIA_URL = f'https://{MEDIA_CLOUDFRONT_DOMAIN}/{MEDIA_LOCATION}'
MEDIA_ACL = None
MEDIA_AWS_ACCESS_KEY_ID = env("MEDIA_AWS_ACCESS_KEY_ID", default=AWS_ACCESS_KEY_ID)
MEDIA_AWS_SECRET_ACCESS_KEY = env("MEDIA_AWS_SECRET_ACCESS_KEY", default=AWS_SECRET_ACCESS_KEY)

WAGTAIL_THEME_PATH = STATIC_URL + "/css/themes"

try:
    from .local import *
except ImportError:
    pass
