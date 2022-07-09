from abc import abstractmethod
from wagtail.core.blocks import CharBlock, PageChooserBlock, StructBlock, URLBlock


class NavLinkBlock(StructBlock):
    title = CharBlock(label="title", required=True)

    @property
    @abstractmethod
    def link(self):
        pass

    class Meta:
        icon = 'link'
        abstract = True


class PageNavLinkBlock(NavLinkBlock):
    link = PageChooserBlock(label="link", required=True)


class URLNavLinkBlock(NavLinkBlock):
    link = URLBlock(label="link", required=True)


class PositionBlock(StructBlock):

    class Meta:
        abstract = True


class RepresentativePositionBlock(PositionBlock):
    body = CharBlock(label="Body", required=True)
    seat = CharBlock(label="Seat", required=True)