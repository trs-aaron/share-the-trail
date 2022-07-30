from django import template

register = template.Library()


@register.inclusion_tag('sharethetrail/snippets/map.html')
def include_map(map_snippet):
    return {
        'map': map_snippet.map,
    }