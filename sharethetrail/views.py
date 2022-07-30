from django.shortcuts import render
from sharethetrail.models.campaign import get_campaign_site_context


def render_with_campaign_site_context(request, template_name, context=None, status=200):
    if context is None:
        context = {}

    context['campaign_site'] = get_campaign_site_context(request)

    return render(request=request, template_name=template_name, context=context, status=status)


def error_400(request, exception):
    context = {
        'error_title': 'Bad Request',
        'error_msg': 'Sorry, your request is malformed',
    }

    return render_with_campaign_site_context(request, 'sharethetrail/error/error.html', context, 400)


def error_403(request, exception):
    context = {
        'error_title': 'Blocked',
        'error_msg': 'Sorry, this page is not accessible by you.',
    }

    return render_with_campaign_site_context(request, 'sharethetrail/error/error.html', context, 403)


def error_404(request, exception):
    context = {
        'error_title': 'Page Not Found',
        'error_msg': 'Sorry, this page could not be found.',
    }

    return render_with_campaign_site_context(request, 'sharethetrail/error/error.html', context, 404)


def error_500(request):
    context = {
        'error_title': 'Internal Server Error',
        'error_msg': 'Sorry, there seems to be an error. Please try again soon.',
    }

    return render_with_campaign_site_context(request, 'sharethetrail/error/error.html', context, 500)