from django.conf import settings
from django.forms import CheckboxSelectMultiple, Select
from django.db import models as django_models
from django.db.models import CharField, EmailField, ForeignKey, Model, TextField, URLField, UUIDField
from encrypted_model_fields.fields import EncryptedCharField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, ObjectList, TabbedInterface
from wagtail.fields import StreamField
from wagtail.models import Site
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.models import Document
from sharethetrail.blocks import CAMPAIGN_POSITION_BLOCKS, NAV_LINK_BLOCKS
from sharethetrail.blocks.campaign import ImportantDateBlock
from xml.dom import minidom

THEMES = getattr(settings, 'SHARETHETRAIL_THEMES', list())
DEFAULT_THEME = getattr(settings, 'SHARETHETRAIL_DEFAULT_THEME')

CAMPAIGN_TYPES = [
    ('candidate', 'Candidate'),
    ('referendum ', 'Referendum'),
]


class Candidate(Model):
    name_prefix = CharField(db_column='name_prefix', max_length=100, blank=True, null=True)
    first_name = CharField(db_column='name_first', max_length=100)
    middle_name = CharField(db_column='name_middle', max_length=100, blank=True, null=True)
    last_name = CharField(db_column='name_last', max_length=100)
    name_suffix = CharField(db_column='name_suffix', max_length=100, blank=True, null=True)
    bio_statement = TextField(db_column='statement_bio', blank=True, null=True)

    admin_panels = [
        MultiFieldPanel(
            [
                FieldPanel('name_prefix', heading='Prefix', help_text='Candidates name prefix'),
                FieldPanel('first_name', heading='First', help_text='Candidates first name'),
                FieldPanel('middle_name', heading='Middle', help_text='Candidates middle name'),
                FieldPanel('last_name', heading='Last', help_text='Candidates last name'),
                FieldPanel('name_suffix', heading='Suffix', help_text='Candidates name suffix'),
            ],
            heading='Name',
        ),
        MultiFieldPanel(
            [
                FieldPanel('bio_statement', heading='Bio', help_text='Candidates first name'),
            ],
            heading='Statements',
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(admin_panels, heading='Candidate'),
    ])

    @property
    def full_name(self):
        name = ''

        if self.name_prefix:
            name = (f'{name} ' if name else '') + self.name_prefix

        if self.first_name:
            name = (f'{name} ' if name else '') + self.first_name

        if self.middle_name:
            name = (f'{name} ' if name else '') + self.middle_name

        if self.last_name:
            name = (f'{name} ' if name else '') + self.last_name

        if self.name_suffix:
            name = (f'{name} ' if name else '') + self.name_suffix

        return name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Issue(Model):
    name = CharField(db_column='name', max_length=250)
    summary = TextField(db_column='summary', blank=True, null=True)

    admin_panels = [
        MultiFieldPanel(
            [
                FieldPanel('name', heading='Name', help_text='Issue name'),
                FieldPanel('summary', heading='Summary', help_text='Issue summary'),
            ],
            heading='Description',
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(admin_panels, heading='Issue'),
    ])

    def __str__(self):
        return self.name


class Campaign(Model):
    name = CharField(db_column='name', max_length=100, blank=True, null=True)
    campaign_type = CharField(db_column='campaign_type', max_length=100, blank=True, null=True)
    candidate = ForeignKey(Candidate, db_column='candidate', related_name='+', blank=True, null=True, on_delete=django_models.SET_NULL)
    contact_email = EmailField(db_column='email_contact', blank=True, null=True)
    media_email = EmailField(db_column='email_media', blank=True, null=True)
    donation_url = URLField(db_column='url_donation', blank=True, null=True)
    twitter_url = URLField(db_column='url_twitter', blank=True, null=True)
    facebook_url = URLField(db_column='url_facebook', blank=True, null=True)
    instagram_url = URLField(db_column='url_instagram', blank=True, null=True)
    youtube_url = URLField(db_column='url_youtube', blank=True, null=True)
    vimeo_url = URLField(db_column='url_vimeo', blank=True, null=True)
    action_network_api_key = EncryptedCharField(db_column='api_key_action_network', max_length=50, blank=True, null=True)

    election_position = StreamField(
        CAMPAIGN_POSITION_BLOCKS,
        db_column='election_position',
        min_num=0,
        max_num=1,
        blank=True,
        null=True,
        use_json_field=True,
    )

    important_dates = StreamField(
        [
            ('important_date', ImportantDateBlock()),
        ],
        db_column='dates_important',
        min_num=0,
        blank=True,
        null=True,
        use_json_field=True,
    )

    admin_panels = [
        MultiFieldPanel(
            [
                FieldPanel('name', heading='Campaign Name', help_text='Campaign name'),
                FieldPanel('campaign_type', heading='Campaign Type', help_text='Type of campaign', widget=Select(choices=CAMPAIGN_TYPES)),
                FieldPanel('candidate', heading='Candidate', help_text='Candidate'),
                FieldPanel('election_position', heading='Position', help_text='Position being sought'),
            ],
            heading='Campaign Information',
        ),
        FieldPanel('important_dates', heading='Important Dates', help_text='Important dates'),
        MultiFieldPanel(
            [
                FieldPanel('contact_email', heading='Email - General', help_text='Email for general inquiries'),
                FieldPanel('media_email', heading='Email - Media', help_text='Email for media inquiries'),
            ],
            heading='Contact Information',
        ),
        MultiFieldPanel(
            [
                FieldPanel('donation_url', heading='Donation', help_text='Donation page URL'),
                FieldPanel('twitter_url', heading='Twitter', help_text='Twitter page URL'),
                FieldPanel('facebook_url', heading='Facebook', help_text='Facebook page URL'),
                FieldPanel('instagram_url', heading='Instagram', help_text='Instagram page URL'),
                FieldPanel('youtube_url', heading='Youtube', help_text='Youtube page URL'),
                FieldPanel('vimeo_url', heading='Vimeo', help_text='Vimeo page URL'),
            ],
            heading='External Links',
        ),
        MultiFieldPanel(
            [
                FieldPanel('action_network_api_key', heading='Action Network API Key', help_text='API Key to integrate with Action Network'),
            ],
            heading='Integrations',
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(admin_panels, heading='Campaign'),
    ])

    def __str__(self):
        return self.name


class AnalyticsMixin(Model):
    google_tag_id = CharField(db_column='analytics_google_tag_id', max_length=30, blank=True, null=True)
    aws_app_monitor_id = UUIDField(db_column='aws_app_monitor_id', max_length=30, blank=True, null=True)

    edit_panels = [
        MultiFieldPanel(
            [
                FieldPanel('google_tag_id', heading='Google Tag ID', help_text='Google analytics tag id'),
                FieldPanel('aws_app_monitor_id', heading='AWS App Monitor ID', help_text='AWS cloud watch app monitor id'),
            ],
            heading='Analytics',
        ),
    ]

    class Meta:
        abstract = True


class CampaignSite(ClusterableModel, AnalyticsMixin):
    name = CharField(db_column='name', max_length=100)
    campaign = ForeignKey(Campaign, db_column='campaign', related_name='+', on_delete=django_models.CASCADE)
    sites = ParentalManyToManyField(Site, related_name='campaign_sites')
    paid_for_by = CharField(db_column='paid_for_by', max_length=100, blank=True, null=True)
    theme = CharField(db_column='site_theme', max_length=100, blank=True, null=True)
    title = CharField(db_column='site_title', max_length=100, blank=True, null=True)
    fav_icon = ForeignKey(Document, db_column='fav_icon', blank=True, null=True, related_name='+', on_delete=django_models.SET_NULL)
    top_nav_logo = ForeignKey(Document, db_column='logo_top_nav', blank=True, null=True, related_name='+', on_delete=django_models.SET_NULL)

    top_nav_links = StreamField(
        NAV_LINK_BLOCKS,
        db_column='links_top_nav',
        min_num=0,
        max_num=4,
        blank=True,
        null=True,
        use_json_field=True,
    )

    footer_links = StreamField(
        NAV_LINK_BLOCKS,
        db_column='links_footer',
        min_num=0,
        max_num=4,
        blank=True,
        null=True,
        use_json_field=True,
    )

    admin_panels = [
        MultiFieldPanel(
            [
                FieldPanel('name', heading='Name', help_text='Name'),
                FieldPanel('campaign', heading='Campaign', help_text='Campaign'),
                FieldPanel('sites', heading='Sites', help_text='Sites', widget=CheckboxSelectMultiple),
            ],
            heading='',
        ),
        MultiFieldPanel(
            [
                FieldPanel('theme', heading='Theme', help_text='Site theme', widget=Select(choices=THEMES)),
                FieldPanel('title', heading='Title', help_text='Site title'),
                FieldPanel('paid_for_by', heading='Paid for By', help_text='Text to display for Paid for By'),
                DocumentChooserPanel('fav_icon', heading='Favicon', help_text='Site Favicon'),
            ],
            heading='Site Display',
        ),
        MultiFieldPanel(
            [
                DocumentChooserPanel('top_nav_logo', heading='Top Navigation', help_text='Logo used in top navigation'),
            ],
            heading='Logos',
        ),
        FieldPanel('top_nav_links', heading='Top Navigation Links', help_text='Top navigation links'),
        FieldPanel('footer_links', heading='Footer Links', help_text='Footer links'),
    ]

    external_panels = AnalyticsMixin.edit_panels

    edit_handler = TabbedInterface([
        ObjectList(admin_panels, heading='Campaign Site'),
        ObjectList(external_panels, heading='External'),
    ])

    def __str__(self):
        return self.name


class CampaignIssue(Model):
    campaign = ForeignKey(Campaign, db_column='campaign', related_name='+', on_delete=django_models.CASCADE)
    issue = ForeignKey(Issue, db_column='issue', related_name='+', on_delete=django_models.PROTECT)
    title = CharField(db_column='title', max_length=250, blank=True, null=True)
    summary_statement = TextField(db_column='statement_summary', blank=True, null=True)
    full_statement = TextField(db_column='statement_full', blank=True, null=True)

    admin_panels = [
        MultiFieldPanel(
            [
                FieldPanel('campaign', heading='Campaign', help_text='Campaign'),
                FieldPanel('issue', heading='Issue', help_text='Issue'),
            ],
            heading='',
        ),
        MultiFieldPanel(
            [
                FieldPanel('summary_statement', heading='Summary', help_text='Short statement about issue'),
                FieldPanel('full_statement', heading='Full', help_text='Full statement about issue'),
            ],
            heading='Statements',
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(admin_panels, heading='Campaign Issue'),
    ])

    def __str__(self):
        return f'{self.campaign } - {self.issue}/'


def get_analytics_context(request):
    site = Site.find_for_request(request)
    campaign_site = site.campaign_sites.select_related('campaign__candidate').first()

    analytics_context = {
        'goggle_tag_id': DEFAULT_THEME,
        'aws_app_monitor_id': None,
        'aws_rum_region': getattr(settings, 'AWS_CW_RUM_REGION', None),
        'aws_rum_client_url': getattr(settings, 'AWS_CW_RUM_CLIENT_URL', None),
        'aws_rum_endpoint_url': getattr(settings, 'AWS_CW_RUM_ENDPOINT_URL', None),
        'aws_rum_role_arn': getattr(settings, 'AWS_CW_RUM_ROLE_ARN', None),
        'aws_rum_identity_pool_id': getattr(settings, 'AWS_CW_RUM_IDENTITY_POOL_ID', None),
    }

    if campaign_site is not None:
        analytics_context['google_tag_id'] = getattr(campaign_site, 'google_tag_id', None)
        analytics_context['aws_app_monitor_id'] = getattr(campaign_site, 'aws_app_monitor_id', None)

    return analytics_context

def get_campaign_site(request):
    site = Site.find_for_request(request)
    return site.campaign_sites.select_related('campaign__candidate').first()

def get_campaign(request):
    campaign_site = get_campaign_site(request)
    return campaign_site.campaign

def get_candidate(request):
    campaign = get_campaign(request)
    return campaign.candidate

def get_campaign_site_context(request):
    campaign_site = get_campaign_site(request)

    site_context = {
        'theme': DEFAULT_THEME,
        'title': None,
        'fav_icon': None,
        'top_nav_logo_svg': None,
        'top_nav_links': [],
        'footer_links': [],
        'paid_for_by': None,
        'campaign': None,
        'candidate': None,
        'election_position': None,
        'important_dates': None,
    }

    if campaign_site is not None:
        site_context['theme'] = getattr(campaign_site, 'theme', DEFAULT_THEME)
        site_context['title'] = getattr(campaign_site, 'title', None)
        site_context['fav_icon'] = campaign_site.fav_icon
        site_context['top_nav_logo_svg'] = minidom.parse(campaign_site.top_nav_logo.file).toxml() if campaign_site.top_nav_logo else None
        site_context['top_nav_links'] = list(map(lambda l: l.value, campaign_site.top_nav_links))
        site_context['footer_links'] = list(map(lambda l: l.value, campaign_site.footer_links))
        site_context['paid_for_by'] = campaign_site.paid_for_by
        site_context['campaign'] = campaign_site.campaign
        site_context['candidate'] = campaign_site.campaign.candidate
        site_context['election_position'] = campaign_site.campaign.election_position[0].value
        site_context['important_dates'] = list(map(lambda d: d.value, campaign_site.campaign.important_dates)) if campaign_site.campaign.important_dates else None

    return site_context


class CampaignSitePageMixin:

    def get_context(self, request):
        context = super(CampaignSitePageMixin, self).get_context(request)
        context['campaign_site'] = get_campaign_site_context(request)
        return context

    class Meta:
        abstract = True