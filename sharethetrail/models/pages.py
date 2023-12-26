from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from coderedcms.models import CoderedPage
from sharethetrail.blocks import LAYOUT_BLOCKS
from sharethetrail.models.campaign import get_analytics_context, get_campaign_site_context
from sharethetrail.models.form_pages import ContactPage, SignUpPage


class CampaignSitePageMixin:

    def get_context(self, request):
        context = super(CampaignSitePageMixin, self).get_context(request)
        context['analytics'] = get_analytics_context(request)
        context['campaign_site'] = get_campaign_site_context(request)
        return context

    class Meta:
        abstract = True


class WebPage(CampaignSitePageMixin, CoderedPage):
    template = 'sharethetrail/pages/web_page.html'

    body = StreamField(
        LAYOUT_BLOCKS,
        null=True,
        blank=True,
        use_json_field=True,
    )

    body_content_panels = [
        FieldPanel('body'),
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
    template = 'sharethetrail/pages/home_page.html'

    body = StreamField(
        LAYOUT_BLOCKS,
        null=True,
        blank=True,
        use_json_field=True,
    )

    body_content_panels = [
        FieldPanel('body'),
    ]

    subpage_types = [
        WebPage,
        ContactPage,
        SignUpPage,
    ]

    @property
    def body_preview(self):
        body = str(self.body).replace('>', '> ')
        body = strip_tags(body)
        preview = body[:200] + "..." if len(body) > 200 else body
        return mark_safe(preview)

    class Meta:
        verbose_name = 'Home Page'