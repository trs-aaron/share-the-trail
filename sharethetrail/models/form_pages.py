from django.db import models
from django.forms import BoundField, BooleanField, CharField, EmailField, Form, Textarea
from django.http.request import QueryDict
from django.shortcuts import render
from django.utils.datastructures import MultiValueDict
from coderedcms.models import CoderedPage
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from sharethetrail.models.campaign import CampaignSitePageMixin, get_campaign
from sharethetrail.emails.email_templates import FormSubmissionEmail


BoundField.has_error = property(lambda self: self.errors)
BoundField.has_valid_value = property(lambda self: self.data and not self.has_error)


class BaseForm(Form):
    __processed__ = False

    @property
    def processed(self):
        return self.__processed__

    def process(self, *args, **kwargs):
        self.__processed__ = True

    def clean_initial_data(self):
        cleaned_data = MultiValueDict()

        for field, value in self.initial.items():
            if field in self.fields:
                cleaned_data[field] = self.fields[field].to_python(value)

        self.initial = cleaned_data

    class Meta:
        abstract = True


class BaseFormPage(CampaignSitePageMixin, CoderedPage):
    form_title = models.CharField(db_column='title_form', max_length=250)
    success_message = models.CharField(db_column='message_success', max_length=250)

    body_content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('form_title', heading='Title', help_text='Form title'),
                FieldPanel('success_message', heading='Success Message', help_text='Message displayed when form is successfully submitted'),
            ],
            heading='Form',
        )
    ]

    def serve(self, request):
        if request.method == 'POST' :
            form = self.get_form(data=request.POST.copy())

            if form.is_valid():
                campaign = get_campaign(request)
                contact_email = campaign.contact_email if campaign is not None else None
                form.process(send_to=contact_email)
                return self.render_success(request, form)
        else:
            form = self.get_form(initial=request.GET.copy())

        return self.render_form(request, form)

    def get_form(self, data=None, initial=None):
        if data is not None:
            return self.FormMeta.form_class(data=data)

        if initial is not None:
            form = self.FormMeta.form_class(initial=initial)
            form.clean_initial_data()
            return form

        return self.FormMeta.form_class()

    def handle_post(self, data):
        pass

    def render_form(self, request, form):
        context = super(BaseFormPage, self).get_context(request)
        context['page'] = self
        context['form'] = form
        return render(request, self.FormMeta.form_template, context)

    def render_success(self, request, form=None):
        context = super(BaseFormPage, self).get_context(request)
        context['page'] = self
        context['form'] = form
        return render(request, self.FormMeta.success_template, context)

    class Meta:
        abstract = True

    class FormMeta:
        form_class = None
        form_template = None
        success_template = None


class ContactForm(BaseForm):
    first_name = CharField(label='first name')
    last_name = CharField(label='last name')
    email = EmailField(label='email')
    phone = CharField(label='phone', required=False)
    message = CharField(label='message', widget=Textarea)

    def process(self, send_to, *args, **kwargs):
        title = 'New Message Received'

        subject = 'New Message from {} {}'.format(
            self.cleaned_data.get('first_name', None),
            self.cleaned_data.get('last_name', None),
        )

        email = FormSubmissionEmail(
            form=self,
            to_email=send_to,
            subject=subject,
            title=title,
        )

        email.send()

        super(ContactForm, self).process(send_to)


class ContactPage(BaseFormPage):

    class Meta:
        verbose_name = 'Contact Page'

    class FormMeta:
        form_class = ContactForm
        form_template = 'sharethetrail/pages/forms/contact/form_page.html'
        success_template = 'sharethetrail/pages/forms/contact/form_page.html'


class SignUpForm(BaseForm):
    first_name = CharField(label='first name')
    last_name = CharField(label='last name')
    email = EmailField(label='email')
    phone = CharField(label='phone', required=False)

    communication_email = BooleanField(label='receive campaign emails', required=False)
    communication_text = BooleanField(label='receive campaign texts', required=False)

    merchandise_yard_sign = BooleanField(label='request yard sign', required=False)

    volunteer_canvass = BooleanField(label='knock on doors', required=False)
    volunteer_call = BooleanField(label='call voters', required=False)
    volunteer_text = BooleanField(label='text voters', required=False)
    volunteer_write_postcards = BooleanField(label='write postcards', required=False)
    volunteer_host_event = BooleanField(label='host event', required=False)

    def process(self, send_to, *args, **kwargs):
        title = 'New Sign Up Request Received'

        subject = 'New Sign Up Request from {} {}'.format(
            self.cleaned_data.get('first_name', None),
            self.cleaned_data.get('last_name', None),
        )

        email = FormSubmissionEmail(
            form=self,
            to_email=send_to,
            subject=subject,
            title=title,
        )

        email.send()

        super(SignUpForm, self).process(send_to)


class SignUpPage(BaseFormPage):
    form_title = models.CharField(db_column='title', max_length=250)
    success_message = models.CharField(db_column='message_success', max_length=250)
    communication_enabled = models.BooleanField(db_column='type_communication_enabled')
    merchandise_enabled = models.BooleanField(db_column='type_merchandise_enabled')
    volunteer_enabled = models.BooleanField(db_column='type_volunteer_enabled')

    body_content_panels = BaseFormPage.body_content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('communication_enabled', heading='Communication', help_text='Enable sign ups for communications'),
                FieldPanel('merchandise_enabled', heading='Merchandise', help_text='Enable sign ups for merchandise requests'),
                FieldPanel('volunteer_enabled', heading='Volunteer', help_text='Enable sign ups for volunteering'),
            ],
            heading='Sign Up Types',
        ),
    ]

    class Meta:
        verbose_name = 'Sign Up Page'

    class FormMeta:
        form_class = SignUpForm
        form_template = 'sharethetrail/pages/forms/sign_up/form_page.html'
        success_template = 'sharethetrail/pages/forms/sign_up/form_page.html'
