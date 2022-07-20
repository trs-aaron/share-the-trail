from django.conf import settings
from django.forms import CheckboxSelectMultiple, Select
from django.db import models as django_models
from django.db.models import CharField, DateField, EmailField, ForeignKey, ManyToManyField, Model, OneToOneField, TextField, URLField
from encrypted_model_fields.fields import EncryptedCharField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, ObjectList, StreamFieldPanel, TabbedInterface
from wagtail.core.fields import StreamField
from wagtail.core.models import Site
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.models import Document
from coderedcms import models as codered_models
from sharethetrail.blocks import ImportantDateBlock, PageNavLinkBlock, RepresentativePositionBlock, URLNavLinkBlock
from xml.dom import minidom

THEMES = getattr(settings, 'SHARETHETRAIL_THEMES', list())
DEFAULT_THEME = getattr(settings, 'SHARETHETRAIL_DEFAULT_THEME')

CAMPAIGN_TYPES = [
    ('candidate', 'Candidate'),
    ('referendum ', 'Referendum'),
]


class Candidate(Model):
    first_name = CharField(db_column='name_first', max_length=100)
    middle_name = CharField(db_column='name_middle', max_length=100, blank=True, null=True)
    last_name = CharField(db_column='name_last', max_length=100)
    bio_statement = TextField(db_column='statement_bio', blank=True, null=True)

    admin_panels = [
        MultiFieldPanel(
            [
                FieldPanel('first_name', heading='First', help_text='Candidates first name'),
                FieldPanel('middle_name', heading='Middle', help_text='Candidates middle name'),
                FieldPanel('last_name', heading='Last', help_text='Candidates last name'),
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
        [
            ('representative', RepresentativePositionBlock()),
        ],
        db_column='election_position',
        min_num=0,
        max_num=1,
        blank=True,
        null=True,
    )

    important_dates = StreamField(
        [
            ('important_date', ImportantDateBlock()),
        ],
        db_column='dates_important',
        min_num=0,
        blank=True,
        null=True,
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


class CampaignSite(ClusterableModel):
    name = CharField(db_column='name', max_length=100,)
    campaign = ForeignKey(Campaign, db_column='campaign', related_name='+', on_delete=django_models.CASCADE)
    sites = ParentalManyToManyField(Site, related_name='campaign_sites')
    paid_for_by = CharField(db_column='paid_for_by', max_length=100, blank=True, null=True)
    theme = CharField(db_column='site_theme', max_length=100, blank=True, null=True)
    title = CharField(db_column='site_title', max_length=100, blank=True, null=True)
    fav_icon = ForeignKey(Document, db_column='fav_icon', blank=True, null=True, related_name='+', on_delete=django_models.SET_NULL)
    top_nav_logo = ForeignKey(Document, db_column='logo_top_nav', blank=True, null=True, related_name='+', on_delete=django_models.SET_NULL)

    top_nav_links = StreamField(
        [
            ('page_link', PageNavLinkBlock()),
            ('url_link', URLNavLinkBlock()),
        ],
        db_column='links_top_nav',
        min_num=0,
        max_num=4,
        blank=True,
        null=True,
    )

    footer_links = StreamField(
        [
            ('page_link', PageNavLinkBlock()),
            ('url_link', URLNavLinkBlock()),
        ],
        db_column='links_footer',
        min_num=0,
        max_num=4,
        blank=True,
        null=True,
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

    edit_handler = TabbedInterface([
        ObjectList(admin_panels, heading='Campaign Site'),
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


class CampaignSitePageMixin:

    def get_context(self, request):
        context = super(CampaignSitePageMixin, self).get_context(request)
        site = Site.find_for_request(request)
        # campaign_site = CampaignSite.objects.select_related('campaign').filter(sites__in=site).first()
        campaign_site = site.campaign_sites.select_related('campaign').first()

        site_context = {
            'theme': DEFAULT_THEME,
            'title': None,
            'fav_icon': None,
            'top_nav_logo_svg': None,
            'top_nav_links': [],
            'footer_links': [],
            'paid_for_by': None,
            'campaign': None,
        }

        if campaign_site is not None:
            site_context['theme'] = getattr(campaign_site, 'theme', DEFAULT_THEME)
            site_context['title'] = getattr(campaign_site, 'title', None)
            site_context['fav_icon'] = campaign_site.fav_icon
            site_context['top_nav_logo_svg'] = minidom.parse(campaign_site.top_nav_logo.file).toxml() if campaign_site.top_nav_logo else None
            site_context['top_nav_links'] = campaign_site.top_nav_links
            site_context['footer_links'] = campaign_site.footer_links
            site_context['paid_for_by'] = campaign_site.paid_for_by
            site_context['campaign'] = campaign_site.campaign

        context['campaign_site'] = site_context

        return context

    class Meta:
        abstract = True


class WebPage(CampaignSitePageMixin, codered_models.CoderedWebPage):
    template = 'sharethetrail/web_page.html'

    class Meta:
        verbose_name = 'Web Page'


# class ArticlePage(CampaignSitePageMixin, codered_models.CoderedArticlePage):
#     template = 'sharethetrail/web_page.html'
#
#     class Meta:
#         verbose_name = 'Article Page'
#         ordering = ['-first_published_at']


# class ArticleIndexPage(CampaignSitePageMixin, codered_models.CoderedArticleIndexPage):
#     template = 'sharethetrail/web_page.html'
#
#     subpage_types = [
#         ArticlePage,
#     ]
#
#     class Meta:
#         verbose_name = 'Article Index Page'


# class EventPage(CampaignSitePageMixin, codered_models.CoderedEventPage):
#
#     subpage_types = [
#         WebPage,
#     ]


# class EventIndexPage(CampaignSitePageMixin, codered_models.CoderedEventPage):
#
#     subpage_types = [
#         EventPage,
#     ]


class HomePage(WebPage):
    template = 'sharethetrail/home_page.html'

    subpage_types = [
        WebPage,
    ]

    class Meta:
        verbose_name = 'Home Page'
