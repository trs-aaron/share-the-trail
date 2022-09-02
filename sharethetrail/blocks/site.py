from wagtail.blocks import BooleanBlock, CharBlock, EmailBlock, PageChooserBlock, StructBlock, StructValue, URLBlock


class NavLinkBlock(StructBlock):
    title = CharBlock(label='title', required=True)

    class Meta:
        abstract = True


class PageNavLinkValue(StructValue):
    is_external_link = False

    def href(self):
        return self['page'].url if self['page'] is not None else None


class PageNavLinkBlock(NavLinkBlock):
    page = PageChooserBlock(label='Page', required=True)

    class Meta:
        label = 'Page Navigation Link'
        icon = 'link'
        value_class = PageNavLinkValue


class URLNavLinkValue(StructValue):
    is_external_link = False

    def href(self):
        return self['url']


class URLNavLinkBlock(NavLinkBlock):
    url = URLBlock(label='Link', required=True)
    is_external_link = BooleanBlock(label='Is External', required=False)

    class Meta:
        label = 'URL Navigation Link'
        icon = 'link'
        value_class = URLNavLinkValue


class EmailNavLinkValue(StructValue):
    is_external_link = False

    def href(self):
        address = self['email_address']
        return f'mailto:{address}' if address is not None else None


class EmailNavLinkBlock(NavLinkBlock):
    email_address = EmailBlock(label='Email Address', required=True)

    class Meta:
        label = 'Email Navigation Link'
        icon = 'link'
        value_class = EmailNavLinkValue


class PhoneNavLinkValue(StructValue):
    is_external_link = False

    def href(self):
        number = self['phone_number']
        return f'tel:{number}' if number is not None else None


class PhoneNavLinkBlock(NavLinkBlock):
    phone_number = CharBlock(label='Phone Number', required=True)

    class Meta:
        label = 'Phone Navigation Link'
        icon = 'link'
        value_class = PhoneNavLinkValue


class SMSNavLinkValue(StructValue):
    is_external_link = False

    def href(self):
        number = self['phone_number']
        return f'sms:{number}' if number is not None else None


class SMSNavLinkBlock(NavLinkBlock):
    phone_number = CharBlock(label='Phone Number', required=True)

    class Meta:
        label = 'Text Message Navigation Link'
        icon = 'link'
        value_class = SMSNavLinkValue