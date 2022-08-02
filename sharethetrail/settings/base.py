import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

INSTALLED_APPS = [
    "sharethetrail",
    "coderedcms",
    "bootstrap4",
    "modelcluster",
    "taggit",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.table_block",
    "wagtail.core",
    "wagtail.documents",
    "wagtail.embeds",
    "wagtail.images",
    "wagtail.users",
    "wagtail.search",
    "wagtail.sites",
    "wagtail.snippets",
    "wagtail.admin",
    "wagtailseo",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "encrypted_model_fields",
    "corsheaders",
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.contrib.migrations",
    "health_check.contrib.psutil",
    "health_check.storage",
]

MIDDLEWARE = [
    "wagtailcache.cache.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "wagtailcache.cache.FetchFromCacheMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https:\/\/\w+\.sharethetrail\.net$",
    r"^https:\/\/\w+\.sharethetrail\.email$",
    r"^https:\/\/\w+\.sharethetrail\.run$",
    r"^https:\/\/\w+\.sharethetrail\.democrat$",
    r"^https:\/\/\w+\.sharethetrail\.republican$",
    r"^https:\/\/www\.google-analytics\.com$",
    r"^https:\/\/www\.googletagmanager\.com$",
    r"^https:\/\/cognito-identity\.\w+-\w+-\w+\.amazonaws\.com$",
    r"^https:\/\/dataplane\.rum\.\w+-\w+-\w+\.amazonaws\.com$",
    r"^https:\/\/sts\.\w+-\w+-\w+\.amazonaws\.com$",
]

ROOT_URLCONF = "sharethetrail.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": False,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

WSGI_APPLICATION = "sharethetrail.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
TAGGIT_CASE_INSENSITIVE = True

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

SHARETHETRAIL_THEMES = [
    ("share-the-trail_theme-1", "Share The Trail - 1"),
    ("share-the-trail_theme-2", "Share The Trail - 2"),
    ("share-the-trail_theme-3", "Share The Trail - 3"),
]

SHARETHETRAIL_DEFAULT_THEME = "share-the-trail_theme-1"

LOGIN_URL = "wagtailadmin_login"
LOGIN_REDIRECT_URL = "wagtailadmin_home"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

BOOTSTRAP4 = {
    # set to blank since coderedcms already loads jquery and bootstrap
    "jquery_url": "",
    "base_url": "",
    # remove green highlight on inputs
    "success_css_class": ""
}

WAGTAIL_ENABLE_UPDATE_CHECK = False
