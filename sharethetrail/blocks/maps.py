from wagtail.core.blocks import StructBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock


class MapBlock(StructBlock):

    class Meta:
        abstract = True
        label = 'Map'
        icon = 'site'


class ImagePreviewMapBlock(MapBlock):
    preview_image = ImageChooserBlock(label='Preview Image', required=True)
    map_url = URLBlock(label='Map URL', required=True)

    class Meta:
        label = 'Image Preview Map'
        icon = 'site'
        template = 'sharethetrail/blocks/maps/image_preview_map.html'