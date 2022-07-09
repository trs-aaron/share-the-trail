from .base import *

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')
SITE_ID = os.getenv('SITE_ID')
WAGTAIL_SITE_NAME = SITE_ID

ALLOWED_HOSTS = [
    os.getenv('ALLOWED_HOSTS')
]

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtailcache',
    'storages'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': SITE_ID,
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

AWS_STORAGE_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
# STATIC_LOCATION = 'static'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

DEFAULT_FILE_STORAGE = 'dstorages.backends.s3boto3.S3Boto3Storage'
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'

WAGTAIL_THEME_PATH = STATIC_URL + "/css/themes"

try:
    from .local import *
except ImportError:
    pass
