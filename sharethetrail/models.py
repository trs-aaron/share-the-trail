from django.conf import settings
from django.forms import Select
from django.db.models import CharField, DateField, EmailField, ForeignKey, Model, OneToOneField, URLField, SET_NULL
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, ObjectList, StreamFieldPanel, TabbedInterface
from wagtail.core.fields import StreamField
from wagtail.core.models import Site
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.models import Document
from coderedcms import models as codered_models
from sharethetrail.blocks import PageNavLinkBlock, RepresentativePositionBlock, URLNavLinkBlock
from xml.dom import minidom


THEMES = getattr(settings, "SHARETHETRAIL_THEMES", list())


class Campaign(Model):
    first_name = CharField(max_length=100, db_column='name_first', blank=True, null=True)
    middle_name = CharField(max_length=100, db_column='name_middle', blank=True, null=True)
    last_name = CharField(max_length=100, db_column='name_last', blank=True, null=True)
    election_primary_date = DateField(db_column='election_date_primary', blank=True, null=True)
    election_general_date = DateField(db_column='election_date_general', blank=True, null=True)
    site = OneToOneField(Site, on_delete=SET_NULL, blank=True, null=True)
    site_title = CharField(db_column='site_title', max_length=100, blank=True, null=True)
    site_theme = CharField(db_column='site_theme', max_length=100, blank=True, null=True)
    contact_email = EmailField(db_column='email_contact', blank=True, null=True)
    media_email = EmailField(db_column='email_media', blank=True, null=True)
    fav_icon = ForeignKey(Document, blank=True, null=True, related_name='+', on_delete=SET_NULL)
    top_nav_logo = ForeignKey(Document, blank=True, null=True, related_name='+', on_delete=SET_NULL)
    donation_url = URLField(db_column='url_donation', blank=True, null=True)
    twitter_url = URLField(db_column='url_twitter', blank=True, null=True)
    facebook_url = URLField(db_column='url_facebook', blank=True, null=True)
    instagram_url = URLField(db_column='url_instagram', blank=True, null=True)
    youtube_url = URLField(db_column='url_youtube', blank=True, null=True)
    vimeo_url = URLField(db_column='url_vimeo', blank=True, null=True)

    election_position = StreamField(
        [
            ('Representative', RepresentativePositionBlock()),
        ],
        min_num=0,
        max_num=1,
        blank=True,
        null=True,
    )

    top_nav_links = StreamField(
        [
            ('page_link', PageNavLinkBlock()),
            ('url_link', URLNavLinkBlock()),
        ],
        min_num=0,
        max_num=4,
        blank=True,
        null=True,
    )

    candidate_tab_panels = [
        MultiFieldPanel(
            [
                FieldPanel('first_name', heading='First', help_text='Candidates first name'),
                FieldPanel('middle_name', heading='Middle', help_text='Candidates middle name'),
                FieldPanel('last_name', heading='Last', help_text='Candidates last name'),
            ],
            heading="Candidate Name",
        ),
        MultiFieldPanel(
            [
                FieldPanel('election_position', heading='Position', help_text='Position being sought'),
                FieldPanel('election_primary_date', heading='Primary Date', help_text='Date of primary election'),
                FieldPanel('election_general_date', heading='General Date', help_text='Date of general election'),
            ],
            heading='Election Information',
        ),
        MultiFieldPanel(
            [
                FieldPanel('site', heading='Site', help_text='Site'),
                FieldPanel('site_title', heading='Title', help_text='Site title'),
                FieldPanel('site_theme', heading='Theme', help_text='Site theme', widget=Select(choices=THEMES)),
                DocumentChooserPanel('fav_icon'),
                FieldPanel('contact_email', heading='Email - General', help_text='Email for general inquiries'),
                FieldPanel('media_email', heading='Email - Media', help_text='Email for media inquiries'),
            ],
            heading="Site Information",
        ),
    ]

    navigation_tab_panels = [
        StreamFieldPanel('top_nav_links', heading='Top Navigation Links'),
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
                DocumentChooserPanel('top_nav_logo'),
            ],
            heading='Logos',
        )
    ]

    edit_handler = TabbedInterface([
        ObjectList(candidate_tab_panels, heading='Candidate Info'),
        ObjectList(navigation_tab_panels, heading='Navigation'),
    ])


class CampaignPageMixin:

    def get_context(self, request):
        context = super(CampaignPageMixin, self).get_context(request)
        site = Site.find_for_request(request)
        campaign = Campaign.objects.filter(site=site).first()
        campaign.top_nav_logo_svg = minidom.parse(campaign.top_nav_logo.file).toxml() if campaign.top_nav_logo else None
        context['campaign'] = campaign
        context['title'] = campaign.site_title
        context['theme'] = campaign.site_theme
        return context

    class Meta:
        abstract = True


class WebPage(CampaignPageMixin, codered_models.CoderedWebPage):
    template = "sharethetrail/web_page.html"

    class Meta:
        verbose_name = 'Web Page'


# class ArticlePage(CampaignPageMixin, codered_models.CoderedArticlePage):
#     template = "sharethetrail/web_page.html"
#
#     class Meta:
#         verbose_name = 'Article Page'
#         ordering = ['-first_published_at']


# class ArticleIndexPage(CampaignPageMixin, codered_models.CoderedArticleIndexPage):
#     template = "sharethetrail/web_page.html"
#
#     subpage_types = [
#         ArticlePage,
#     ]
#
#     class Meta:
#         verbose_name = 'Article Index Page'


# class EventPage(CampaignPageMixin, codered_models.CoderedEventPage):
#
#     subpage_types = [
#         WebPage,
#     ]


# class EventIndexPage(CampaignPageMixin, codered_models.CoderedEventPage):
#
#     subpage_types = [
#         EventPage,
#     ]


class HomePage(WebPage):
    template = "sharethetrail/home_page.html"

    subpage_types = [
        WebPage,
    ]

    class Meta:
        verbose_name = 'Home Page'
