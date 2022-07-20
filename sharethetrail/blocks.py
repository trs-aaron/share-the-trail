from abc import abstractmethod
from wagtail.core.blocks import CharBlock, DateBlock, PageChooserBlock, StructBlock, URLBlock


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
    link = PageChooserBlock(label="Link", required=True)


class URLNavLinkBlock(NavLinkBlock):
    link = CharBlock(label="Link", required=True)


class ImportantDateBlock(StructBlock):
    date = DateBlock(label="Date", required=True)
    title = CharBlock(label="Title", required=True)


class PositionBlock(StructBlock):

    class Meta:
        abstract = True


class RepresentativePositionBlock(PositionBlock):
    body = CharBlock(label="Body", required=True)
    seat = CharBlock(label="Seat", required=True)
