from abc import abstractmethod
from datetime import datetime
from io import StringIO
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.application import MIMEApplication


def send_email(from_email, to_email, subject, text_content, html_content, attachments=None):
    if to_email is not None:
        to = to_email if isinstance(to_email, (list, tuple)) else [to_email]
    else:
        to = None

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=to,
        attachments=attachments,
    )

    msg.attach_alternative(html_content, "text/html")

    return msg.send()


class BaseEmail:
    from_email = None
    to_emails = ()
    subject = None

    def __init__(self, from_email, to_email, subject=None):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject

    @abstractmethod
    def get_context(self):
        pass

    def get_text_content(self):
        content = render_to_string(self.Meta.text_content_template, self.get_context())
        return content

    def get_html_content(self):
        content = render_to_string(self.Meta.html_content_template, self.get_context())
        return content

    @abstractmethod
    def get_attachments(self):
        pass

    def send(self):
        return send_email(
            from_email=self.from_email,
            to_email=self.to_email,
            subject=self.subject,
            text_content=self.get_text_content(),
            html_content=self.get_html_content(),
            attachments=self.get_attachments(),
        )

    class Meta:
        abstract = True
        html_content_template = None
        text_content_template = None


class FormSubmissionEmail(BaseEmail):
    form = None
    title = None
    description = None
    footer = None

    def __init__(self, form, to_email, subject=None, title=None, description=None, footer=None):
        super().__init__(
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL'),
            to_email=to_email,
            subject=subject,
        )

        self.form = form
        self.title = title
        self.description = description
        self.footer = footer

    def get_context(self):
        context = {
            'title': self.title,
            'description': self.description,
            'footer': self.footer,
            'form_data': list(),
        }

        if self.form is not None:
            for key, field in self.form.declared_fields.items():
                value = self.form.cleaned_data.get(key, None)

                if isinstance(value, bool):
                    value = 'Yes' if value is True else ''

                context['form_data'].append({
                    'field_name': field.label if field.label is not None else key,
                    'field_value': value,
                })

        return context

    def get_attachments(self):
        filename = 'form-submission-data_{}.csv'.format(datetime.now().strftime('%Y%m%d%H%M%S%f'))
        return [MIMEApplication(self.get_form_data_csv(), Name=filename)]

    def get_form_data_csv(self):
        csv_keys_str = ''
        csv_values_str = ''

        if self.form is not None:
            for key, field in self.form.declared_fields.items():
                value = self.form.cleaned_data.get(key, None)

                if isinstance(value, bool):
                    value = 'true' if value is True else 'false'

                if value is None:
                    value = ''

                csv_keys_str += '{},'.format(field.label if field.label is not None else key)
                csv_values_str += '{},'.format(value)

                csv_keys_str.rstrip(',')
                csv_values_str.rstrip(',')

        return StringIO('{}\r\n{}'.format(csv_keys_str, csv_values_str)).read()

    class Meta:
        html_content_template = 'sharethetrail/emails/html/form_submission_email.html'
        text_content_template = 'sharethetrail/emails/text/form_submission_email.txt'
