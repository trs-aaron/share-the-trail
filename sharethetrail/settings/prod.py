import os
from environ import Env
from .base import *

env = Env()
env.read_env()

DEBUG = env('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')
SITE_ID = env.str('SITE_ID', default='test')
ADMIN_HOST = env.str('ADMIN_HOST', default='sharethetrail.net')
WAGTAIL_SITE_NAME = SITE_ID

ALLOWED_HOSTS = [
    '3.137.207.202',
    'sharethetrail.net',
    '.sharethetrail.net',
    'sharethetrail.democrat',
    '.sharethetrail.democrat',
    'sharethetrail.republican',
    '.sharethetrail.republican',
    'sharethetrail.run',
    '.sharethetrail.run',
    '*',
]

CSRF_TRUSTED_ORIGINS = [
    f'https://{ADMIN_HOST}'
]

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtailcache',
    'storages',
    'health_check.contrib.s3boto3_storage',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': SITE_ID,
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env.int('DB_PORT', 5432),
    }
}

AWS_STORAGE_BUCKET_NAME = env('S3_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_CLOUDFRONT_DOMAIN = env.str('MEDIA_HOST', default='media.sharethetrail.net')
AWS_S3_CUSTOM_DOMAIN = AWS_CLOUDFRONT_DOMAIN
AWS_LOCATION = SITE_ID
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
# MEDIA_HOST = env.str('MEDIA_HOST', default='static.sharethetrail.net')
# STATIC_LOCATION = 'static'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_LOCATION = f'{AWS_LOCATION}/media/'
MEDIA_ROOT = f'/{MEDIA_LOCATION}'
MEDIA_URL = f'{AWS_CLOUDFRONT_DOMAIN}/{MEDIA_LOCATION}'

WAGTAIL_THEME_PATH = STATIC_URL + "/css/themes"

try:
    from .local import *
except ImportError:
    pass
