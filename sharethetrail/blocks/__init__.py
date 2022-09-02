from . import campaign
from . import cards
from . import site

from wagtail.blocks import RawHTMLBlock, RichTextBlock
from coderedcms.blocks import CardGridBlock, GridBlock, ReusableContentBlock


HTML_BLOCKS = [
    ('rich_text', RichTextBlock(icon='code', label='Rich Text')),
    ('html', RawHTMLBlock(icon='code', form_classname='monospace', label='HTML')),
]

CARD_GRID_BLOCKS = [
    ('election_info_card', cards.ElectionInformationCardBlock(icon='pick', label='Election Information Card')),
    ('image_card', cards.ImageCardBlock(icon='image', label='Image Card')),
    ('image_page_link_card', cards.ImagePageLinkCardBlock(icon='image', label='Image Page Link Card')),
    ('image_url_link_card', cards.ImageURLLinkCardBlock(icon='image', label='Image URL Link Card')),
    ('issue_flip_card', cards.IssueFlipCardBlock(icon='list-ul', label='Issue Flip Card')),

]

CONTENT_BLOCKS = CARD_GRID_BLOCKS + [
    ('candidate_card', cards.CandidateCardBlock(icon='user', label='Candidate Card')),
    ('reusable_content', ReusableContentBlock()),
] + HTML_BLOCKS

LAYOUT_BLOCKS = [
    ('row', GridBlock(CONTENT_BLOCKS)),
    ('cardgrid', CardGridBlock(CARD_GRID_BLOCKS)),
    ('html', RawHTMLBlock(icon='code', form_classname='monospace', label='HTML')),
]

NAV_LINK_BLOCKS = [
    ('page_link', site.PageNavLinkBlock()),
    ('url_link', site.URLNavLinkBlock()),
    ('email_link', site.EmailNavLinkBlock()),
    ('phone_link', site.PhoneNavLinkBlock()),
    ('sms_link', site.SMSNavLinkBlock()),
]

CAMPAIGN_POSITION_BLOCKS = [
    ('representative', campaign.RepresentativePositionBlock()),
]