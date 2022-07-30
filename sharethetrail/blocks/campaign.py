from wagtail.core.blocks import CharBlock, DateBlock, StructBlock, StructValue


class ImportantDateBlock(StructBlock):
    date = DateBlock(label="Date", required=True)
    title = CharBlock(label="Title", required=True)

    class Meta:
        label = 'Important Date'
        icon = 'date'


class PositionValue(StructValue):

    def heading(self):
        pass

    def subheading(self):
        pass

    class Meta:
        abstract = True


class PositionBlock(StructBlock):

    class Meta:
        abstract = True


class RepresentativePositionValue(PositionValue):

    def heading(self):
        return self['body']

    def subheading(self):
        return self['seat']


class RepresentativePositionBlock(PositionBlock):
    body = CharBlock(label="Body", required=True)
    seat = CharBlock(label="Seat", required=True)

    class Meta:
        label = 'Representative Position'
        icon = 'pick'
        value_class = RepresentativePositionValue
