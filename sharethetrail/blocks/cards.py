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


class SignUpCardBlock(StructBlock):
    title = CharBlock(label='Title', required=True)
    submit_bttn_label = CharBlock(label='Submit Button Label', required=True)
    form_page = PageChooserBlock(label='Form Page', required=True)

    default_communication_email = BooleanBlock(label='Default - Receive Campaign Emails', required=False)
    default_communication_text = BooleanBlock(label='Default - Receive Campaign Texts', required=False)

    default_merchandise_yard_sign = BooleanBlock(label='Default - Request Yard Sign', required=False)

    default_volunteer_canvass = BooleanBlock(label='Default - Knock on Doors', required=False)
    default_volunteer_call = BooleanBlock(label='Default - Call Voters', required=False)
    default_volunteer_text = BooleanBlock(label='Default - Text Voters', required=False)
    default_volunteer_write_postcards = BooleanBlock(label='Default - Write Postcards', required=False)
    default_volunteer_host_event = BooleanBlock(label='Default - Host Event', required=False)

    class Meta:
        label = 'Sign Up Card'
        icon = 'user'
        template = 'sharethetrail/blocks/cards/sign_up_card_block.html'


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
    summary = CharBlock(label='Summary', required=False)
    statement = RichTextBlock(label='Statement', required=True)
    color = CharBlock(label='Color', required=True)
    front_image = ImageChooserBlock(label='Front Image', required=True)
    back_image = ImageChooserBlock(label='Back Image', required=False)

    class Meta:
        label = 'Issue Flip Card'
        icon = 'list-ul'
        template = 'sharethetrail/blocks/cards/issue_flip_card_block.html'


class IWillVoteCardBlock(StructBlock):

    class Meta:
        label = 'I Will Vote Card'
        icon = 'user'
        template = 'sharethetrail/blocks/cards/i_will_vote_card_block.html'
