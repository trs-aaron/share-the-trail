from .campaign_blocks import *
from .card_blocks import *
from .site_blocks import *

from wagtail.core.blocks import RawHTMLBlock, RichTextBlock
from coderedcms.blocks import CardGridBlock, GridBlock, ReusableContentBlock


HTML_BLOCKS = [
    ('rich_text', RichTextBlock(icon='code', label='Rich Text')),
    ('html', RawHTMLBlock(icon='code', form_classname='monospace', label='HTML')),
]

CARD_GRID_BLOCKS = [
    ('election_info_card', ElectionInformationCardBlock(icon='pick', label='Election Information Card')),
    ('image_card', ImageCardBlock(icon='image', label='Image Card')),
    ('image_page_link_card', ImagePageLinkCardBlock(icon='image', label='Image Page Link Card')),
    ('image_url_link_card', ImageURLLinkCardBlock(icon='image', label='Image URL Link Card')),
    ('issue_flip_card', IssueFlipCardBlock(icon='list-ul', label='Issue Flip Card')),

]

CONTENT_BLOCKS = CARD_GRID_BLOCKS + [
    ('candidate_card', CandidateCardBlock(icon='user', label='Candidate Card')),
    ('reusable_content', ReusableContentBlock()),
] + HTML_BLOCKS

LAYOUT_BLOCKS = [
    ('row', GridBlock(CONTENT_BLOCKS)),
    ('cardgrid', CardGridBlock(CARD_GRID_BLOCKS)),
    ('html', RawHTMLBlock(icon='code', form_classname='monospace', label='HTML')),
]

NAV_LINK_BLOCKS = [
    ('page_link', PageNavLinkBlock()),
    ('url_link', URLNavLinkBlock()),
    ('email_link', EmailNavLinkBlock()),
    ('phone_link', PhoneNavLinkBlock()),
    ('sms_link', SMSNavLinkBlock()),
]

CAMPAIGN_POSITION_BLOCKS = [
    ('representative', RepresentativePositionBlock()),
]