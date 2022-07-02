from django.db.models import CharField, DateField, EmailField, TextField, URLField, Model, OneToOneField, SET_NULL
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, ObjectList, TabbedInterface
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import models as wagtail_models
from coderedcms import models as codered_models


class Campaign(Model):
    first_name = CharField(max_length=100, db_column='name_first', blank=True, null=True)
    middle_name = CharField(max_length=100, db_column='name_middle', blank=True, null=True)
    last_name = CharField(max_length=100, db_column='name_last', blank=True, null=True)
    election_office = CharField(max_length=250, db_column='election_office', blank=True, null=True)
    election_primary_date = DateField(db_column='election_date_primary', blank=True, null=True)
    election_general_date = DateField(db_column='election_date_general', blank=True, null=True)
    contact_email = EmailField(db_column='email_contact', blank=True, null=True)
    media_email = EmailField(db_column='email_media', blank=True, null=True)
    top_nav_logo = TextField(db_column='logo_topnav',blank=True, null=True)
    donation_url = URLField(db_column='url_donation', blank=True, null=True)
    twitter_url = URLField(db_column='url_twitter', blank=True, null=True)
    facebook_url = URLField(db_column='url_facebook', blank=True, null=True)
    instagram_url = URLField(db_column='url_instagram', blank=True, null=True)
    youtube_url = URLField(db_column='url_youtube', blank=True, null=True)
    vimeo_url = URLField(db_column='url_vimeo', blank=True, null=True)
    site = OneToOneField(wagtail_models.Site, on_delete=SET_NULL, blank=True, null=True)

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
                FieldPanel('election_office', heading='Office', help_text='Office being sought'),
                FieldPanel('election_primary_date', heading='Primary Date', help_text='Date of primary election'),
                FieldPanel('election_general_date', heading='General Date', help_text='Date of general election'),
            ],
            heading='Election Information',
        ),
        MultiFieldPanel(
            [
                FieldPanel('site', heading='Site', help_text='Site'),
                FieldPanel('contact_email', heading='Email - General', help_text='Email for general inquiries'),
                FieldPanel('media_email', heading='Email - Media', help_text='Email for media inquiries'),
            ],
            heading="Site Information",
        ),
    ]

    navigation_tab_panels = [
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
                FieldPanel('top_nav_logo'),
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
        site = wagtail_models.Site.find_for_request(request)
        context['campaign'] = Campaign.objects.filter(site=site).first()
        return context

    class Meta:
        abstract = True


class WebPage(CampaignPageMixin, codered_models.CoderedWebPage):

    template = "sharethetrail/web_page.html"

    parent_page_types = [
        wagtail_models.Page,
    ]

    class Meta:
        verbose_name = 'Web Page'


class ArticlePage(CampaignPageMixin, codered_models.CoderedArticlePage):

    template = "sharethetrail/web_page.html"

    parent_page_types = [
        WebPage,
    ]

    subpage_types = [
        WebPage,
    ]

    class Meta:
        verbose_name = 'Article Page'
        ordering = ['-first_published_at']


class ArticleIndexPage(CampaignPageMixin, codered_models.CoderedArticleIndexPage):

    template = "sharethetrail/web_page.html"

    parent_page_types = [
        WebPage,
    ]

    subpage_types = [
        ArticlePage,
    ]

    class Meta:
        verbose_name = 'Article Index Page'


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


class LocationPage(CampaignPageMixin, codered_models.CoderedLocationPage):

    template = "sharethetrail/web_page.html"

    parent_page_types = [
        WebPage,
    ]

    subpage_types = [
        ArticlePage,
        ArticleIndexPage,
        # EventPage,
        # EventIndexPage,
        WebPage,
    ]

    class Meta:
        verbose_name = 'Location Page'


class HomePage(WebPage):

    template = "sharethetrail/home_page.html"

    subpage_types = [
        ArticlePage,
        ArticleIndexPage,
        # EventPage,
        # EventIndexPage,
        LocationPage,
        WebPage
    ]

    class Meta:
        verbose_name = 'Home Page'
