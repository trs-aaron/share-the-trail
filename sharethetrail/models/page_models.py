from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from wagtail.core.models import Page, StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from coderedcms.models import CoderedPage
from .campaign_models import get_campaign_site_context
from sharethetrail.blocks import LAYOUT_BLOCKS


class CampaignSitePageMixin:

    def get_context(self, request):
        context = super(CampaignSitePageMixin, self).get_context(request)
        context['campaign_site'] = get_campaign_site_context(request)
        return context

    class Meta:
        abstract = True


class WebPage(CampaignSitePageMixin, CoderedPage):
    template = 'sharethetrail/web_page.html'

    body = StreamField(LAYOUT_BLOCKS, null=True, blank=True)

    body_content_panels = [
        StreamFieldPanel('body'),
    ]

    @property
    def body_preview(self):
        body = str(self.body).replace('>', '> ')
        body = strip_tags(body)
        preview = body[:200] + "..." if len(body) > 200 else body
        return mark_safe(preview)

    class Meta:
        verbose_name = 'Web Page'


class HomePage(CampaignSitePageMixin, CoderedPage):
    template = 'sharethetrail/home_page.html'

    body = StreamField(LAYOUT_BLOCKS, null=True, blank=True)

    body_content_panels = [
        StreamFieldPanel('body'),
    ]

    subpage_types = [
        WebPage,
    ]

    @property
    def body_preview(self):
        body = str(self.body).replace('>', '> ')
        body = strip_tags(body)
        preview = body[:200] + "..." if len(body) > 200 else body
        return mark_safe(preview)

    class Meta:
        verbose_name = 'Home Page'