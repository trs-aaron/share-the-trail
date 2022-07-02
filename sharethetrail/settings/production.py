from .base import *

DEBUG = False

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtailcache',
]

try:
    from .local import *
except ImportError:
    pass
