from wagtail.blocks import BooleanBlock, CharBlock, PageChooserBlock, RichTextBlock, StructBlock, StructValue, URLBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from sharethetrail.models.snippets import MapSnippet

class CandidateCardBlock(StructBlock):
    image = ImageChooserBlock(label='Image', required=True)
    show_position = BooleanBlock(label='Show Position Information', required=False)
    statement = RichTextBlock(label='Statement', required=True)

    class Meta:
        label = 'Candidate Card'
        icon = 'user'
        template = 'sharethetrail/blocks/cards/candidate_card_block.html'


class ElectionInformationCardBlock(StructBlock):
    show_position = BooleanBlock(label='Show Position Information', required=False)
    show_important_dates = BooleanBlock(label='Show Important Dates', required=False)
    map = SnippetChooserBlock(MapSnippet, label='Map', required=False)

    class Meta:
        label = 'Election Information Card'
        icon = 'pick'
        template = 'sharethetrail/blocks/cards/election_information_card_block.html'


class ImageCardBlock(StructBlock):
    image = ImageChooserBlock(label='Image', required=True)

    class Meta:
        label = 'Image Card'
        icon = 'image'
        template = 'sharethetrail/blocks/cards/image_card_block.html'


class ImageLinkCardBlock(ImageCardBlock):

    class Meta:
        template = 'sharethetrail/blocks/cards/image_link_card_block.html'
        abstract = True


class ImagePageLinkCardValue(StructValue):
    is_external_link = False

    def url(self):
        return self['page'].url if self['page'] is not None else None


class ImagePageLinkCardBlock(ImageLinkCardBlock):
    page = PageChooserBlock(label="Page", required=True)

    class Meta:
        label = 'Image Page Link Card'
        icon = 'image'
        value_class = ImagePageLinkCardValue


class ImageURLLinkCardBlock(ImageLinkCardBlock):
    url = URLBlock(label="URL", required=True)
    is_external_link = BooleanBlock(label="Is External", required=False)

    class Meta:
        label = 'Image URL Link Card'
        icon = 'image'


class IssueFlipCardBlock(StructBlock):
    title = CharBlock(label='Title', required=True)
    statement = RichTextBlock(label='Statement', required=True)
    color = CharBlock(label='Color', required=True)
    front_image = ImageChooserBlock(label='Front Image', required=True)
    back_image = ImageChooserBlock(label='Back Image', required=False)

    class Meta:
        label = 'Issue Flip Card'
        icon = 'list-ul'
        template = 'sharethetrail/blocks/cards/issue_flip_card_block.html'
