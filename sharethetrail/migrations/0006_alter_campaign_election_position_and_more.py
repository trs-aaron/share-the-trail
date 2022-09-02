# Generated by Django 4.0.7 on 2022-09-07 03:20

from django.db import migrations
import sharethetrail.models.snippets
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sharethetrail', '0005_contactpage_signuppage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='election_position',
            field=wagtail.fields.StreamField([('representative', wagtail.blocks.StructBlock([('body', wagtail.blocks.CharBlock(label='Body', required=True)), ('seat', wagtail.blocks.CharBlock(label='Seat', required=True))]))], blank=True, db_column='election_position', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='important_dates',
            field=wagtail.fields.StreamField([('important_date', wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock(label='Date', required=True)), ('title', wagtail.blocks.CharBlock(label='Title', required=True))]))], blank=True, db_column='dates_important', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='campaignsite',
            name='footer_links',
            field=wagtail.fields.StreamField([('page_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))])), ('url_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('url', wagtail.blocks.URLBlock(label='Link', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))])), ('email_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('email_address', wagtail.blocks.EmailBlock(label='Email Address', required=True))])), ('phone_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('phone_number', wagtail.blocks.CharBlock(label='Phone Number', required=True))])), ('sms_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('phone_number', wagtail.blocks.CharBlock(label='Phone Number', required=True))]))], blank=True, db_column='links_footer', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='campaignsite',
            name='top_nav_links',
            field=wagtail.fields.StreamField([('page_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))])), ('url_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('url', wagtail.blocks.URLBlock(label='Link', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))])), ('email_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('email_address', wagtail.blocks.EmailBlock(label='Email Address', required=True))])), ('phone_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('phone_number', wagtail.blocks.CharBlock(label='Phone Number', required=True))])), ('sms_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('phone_number', wagtail.blocks.CharBlock(label='Phone Number', required=True))]))], blank=True, db_column='links_top_nav', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('row', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False)), ('column_breakpoint', wagtail.blocks.ChoiceBlock(choices=[('', 'Always expanded'), ('sm', 'sm - Expand on small screens (phone, 576px) and larger'), ('md', 'md - Expand on medium screens (tablet, 768px) and larger'), ('lg', 'lg - Expand on large screens (laptop, 992px) and larger'), ('xl', 'xl - Expand on extra large screens (wide monitor, 1200px)')], help_text='Screen size at which the column will expand horizontally or stack vertically.', required=False, verbose_name='Column Breakpoint'))])), ('column_size', wagtail.blocks.ChoiceBlock(choices=[('', 'Automatically size'), ('12', 'Full row'), ('6', 'Half - 1/2 column'), ('4', 'Thirds - 1/3 column'), ('8', 'Thirds - 2/3 column'), ('3', 'Quarters - 1/4 column'), ('9', 'Quarters - 3/4 column'), ('2', 'Sixths - 1/6 column'), ('10', 'Sixths - 5/6 column'), ('1', 'Twelfths - 1/12 column'), ('5', 'Twelfths - 5/12 column'), ('7', 'Twelfths - 7/12 column'), ('11', 'Twelfths - 11/12 column')], label='Column size', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('map', wagtail.snippets.blocks.SnippetChooserBlock(sharethetrail.models.snippets.MapSnippet, label='Map', required=False))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card')), ('candidate_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True))], icon='user', label='Candidate Card')), ('reusable_content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('content', wagtail.snippets.blocks.SnippetChooserBlock('coderedcms.ReusableContent'))])), ('rich_text', wagtail.blocks.RichTextBlock(icon='code', label='Rich Text')), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], label='Content'))]))], label='Content'))])), ('cardgrid', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default'), ('coderedcms/blocks/cardgrid_group.html', 'Card group - attached cards of equal size'), ('coderedcms/blocks/cardgrid_deck.html', 'Card deck - separate cards of equal size'), ('coderedcms/blocks/cardgrid_columns.html', 'Card masonry - fluid brick pattern')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('map', wagtail.snippets.blocks.SnippetChooserBlock(sharethetrail.models.snippets.MapSnippet, label='Map', required=False))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card'))], label='Content'))])), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='mapsnippet',
            name='map',
            field=wagtail.fields.StreamField([('image_preview_map', wagtail.blocks.StructBlock([('preview_image', wagtail.images.blocks.ImageChooserBlock(label='Preview Image', required=True)), ('map_url', wagtail.blocks.URLBlock(label='Map URL', required=True))]))], blank=True, db_column='map', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='body',
            field=wagtail.fields.StreamField([('row', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False)), ('column_breakpoint', wagtail.blocks.ChoiceBlock(choices=[('', 'Always expanded'), ('sm', 'sm - Expand on small screens (phone, 576px) and larger'), ('md', 'md - Expand on medium screens (tablet, 768px) and larger'), ('lg', 'lg - Expand on large screens (laptop, 992px) and larger'), ('xl', 'xl - Expand on extra large screens (wide monitor, 1200px)')], help_text='Screen size at which the column will expand horizontally or stack vertically.', required=False, verbose_name='Column Breakpoint'))])), ('column_size', wagtail.blocks.ChoiceBlock(choices=[('', 'Automatically size'), ('12', 'Full row'), ('6', 'Half - 1/2 column'), ('4', 'Thirds - 1/3 column'), ('8', 'Thirds - 2/3 column'), ('3', 'Quarters - 1/4 column'), ('9', 'Quarters - 3/4 column'), ('2', 'Sixths - 1/6 column'), ('10', 'Sixths - 5/6 column'), ('1', 'Twelfths - 1/12 column'), ('5', 'Twelfths - 5/12 column'), ('7', 'Twelfths - 7/12 column'), ('11', 'Twelfths - 11/12 column')], label='Column size', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('map', wagtail.snippets.blocks.SnippetChooserBlock(sharethetrail.models.snippets.MapSnippet, label='Map', required=False))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card')), ('candidate_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True))], icon='user', label='Candidate Card')), ('reusable_content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('content', wagtail.snippets.blocks.SnippetChooserBlock('coderedcms.ReusableContent'))])), ('rich_text', wagtail.blocks.RichTextBlock(icon='code', label='Rich Text')), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], label='Content'))]))], label='Content'))])), ('cardgrid', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default'), ('coderedcms/blocks/cardgrid_group.html', 'Card group - attached cards of equal size'), ('coderedcms/blocks/cardgrid_deck.html', 'Card deck - separate cards of equal size'), ('coderedcms/blocks/cardgrid_columns.html', 'Card masonry - fluid brick pattern')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=False)), ('map', wagtail.snippets.blocks.SnippetChooserBlock(sharethetrail.models.snippets.MapSnippet, label='Map', required=False))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card'))], label='Content'))])), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], blank=True, null=True, use_json_field=True),
        ),
    ]
