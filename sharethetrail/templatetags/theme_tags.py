from django import template
from django.conf import settings

register = template.Library()

THEMES = getattr(settings, "SHARETHETRAIL_THEMES", list())
DEFAULT_THEME = getattr(settings, "SHARETHETRAIL_DEFAULT_THEME")


@register.simple_tag()
def theme_css_path(theme):
    if not theme:
        theme = DEFAULT_THEME

    return f'css/{theme}.min.css'
