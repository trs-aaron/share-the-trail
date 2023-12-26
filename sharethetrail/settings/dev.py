from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-8+-j3rwqe6!p4(^q-6254p@r065j(jci(h75$ij$$(u3j6wj&f"
FIELD_ENCRYPTION_KEY = "fNvUX56CncnrOb3T9I_XwuRgeUjc1bZ9EFPOb4zj2n0="
SITE_TYPE = "site"
SITE_ID = "dev"
WAGTAIL_SITE_NAME = SITE_ID

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, ".data/sharethetrail.sqlite3"),
    }
}

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, ".data/media")
MEDIA_URL = "media/"

AWS_S3_REGION_NAME = "us-east-2"

DEFAULT_FROM_EMAIL = "notifications@development.sharethetrail.net"
AWS_SES_REGION_NAME = AWS_S3_REGION_NAME
AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'
AWS_SES_ACCESS_KEY_ID = "AKIAV62DDAU2BIZPHEPG"
AWS_SES_SECRET_ACCESS_KEY = "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"

AWS_CW_RUM_REGION = "us-east-2"
AWS_CW_RUM_CLIENT_URL = "https://client.rum.us-east-1.amazonaws.com/1.5.x/cwr.js"
AWS_CW_RUM_ENDPOINT_URL = "https://dataplane.rum.us-east-2.amazonaws.com"
AWS_CW_RUM_ROLE_ARN = "arn:aws:iam::409773212980:role/sharethetrail-rum-monitor_role"
AWS_CW_RUM_IDENTITY_POOL_ID = "us-east-2:26ce35a5-eb61-4cee-8586-0607e750c22a"

WAGTAIL_THEME_PATH = STATIC_URL + "/css/themes"

try:
    from .local import *
except ImportError:
    pass
