from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-8+-j3rwqe6!p4(^q-6254p@r065j(jci(h75$ij$$(u3j6wj&f"
SITE_ID = 'dev'
WAGTAIL_SITE_NAME = SITE_ID

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "../../data/sharethetrail.sqlite3"),
    }
}

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, "../../data/media")
MEDIA_URL = "media/"

WAGTAIL_THEME_PATH = STATIC_URL + "/css/themes"

try:
    from .local import *
except ImportError:
    pass
