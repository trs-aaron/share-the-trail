from django.db.models import CharField, Model
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from sharethetrail.blocks.maps import ImagePreviewMapBlock

@register_snippet
class MapSnippet(Model):
    name = CharField(max_length=255)
    map = StreamField(
        [
            ('image_preview_map', ImagePreviewMapBlock()),
        ],
        db_column='map',
        min_num=1,
        max_num=1,
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('map'),
    ]

    def __str__(self):
        return self.name