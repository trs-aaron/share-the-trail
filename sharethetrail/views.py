from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt
from wagtail.views import serve
from sharethetrail.models.campaign import get_campaign, get_campaign_site_context


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


@xframe_options_exempt
def external(request, name):
    try:
        template_name = 'sharethetrail/external/{}.html'.format(name)
        return render_with_campaign_site_context(request, template_name)
    except Http404 as e:
        raise Http404


def error_500(request):
    context = {
        'error_title': 'Internal Server Error',
        'error_msg': 'Sorry, there seems to be an error. Please try again soon.',
    }

    return render_with_campaign_site_context(request, 'sharethetrail/error/error.html', context, 500)


class DonateView(View):

    def get(self, request, *args, **kwargs):
        try:
            page_response = serve(request, request.path)
        except Http404:
            page_response = None

        if page_response:
            return page_response
        else:
            campaign = get_campaign(request)

            if campaign is not None and campaign.donation_url is not None:
                return redirect(
                    to=campaign.donation_url,
                    permanent=False,
                )

        raise Http404
