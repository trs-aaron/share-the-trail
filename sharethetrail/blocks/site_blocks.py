from abc import abstractmethod
from wagtail.core.blocks import BooleanBlock, CharBlock, PageChooserBlock, StructBlock, StructValue, URLBlock


class NavLinkBlock(StructBlock):
    title = CharBlock(label="title", required=True)

    class Meta:
        abstract = True


class PageNavLinkValue(StructValue):
    is_external_link = False

    def url(self):
        return self['page'].url if self['page'] is not None else None


class PageNavLinkBlock(NavLinkBlock):
    page = PageChooserBlock(label="Page", required=True)

    class Meta:
        label = 'Page Navigation Link'
        icon = 'link'
        value_class = PageNavLinkValue


class URLNavLinkBlock(NavLinkBlock):
    url = URLBlock(label="Link", required=True)
    is_external_link = BooleanBlock(label="Is External", required=False)

    class Meta:
        label = 'URL Navigation Link'
        icon = 'link'