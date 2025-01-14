# Generated by Django 4.0.6 on 2022-07-27 03:02

from django.db import migrations, models
import django.db.models.deletion
import encrypted_model_fields.fields
import modelcluster.fields
import sharethetrail.models.pages
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('coderedcms', '0030_alter_coderedtag_tag'),
        ('wagtaildocs', '0012_uploadeddocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='name', max_length=100, null=True)),
                ('campaign_type', models.CharField(blank=True, db_column='campaign_type', max_length=100, null=True)),
                ('contact_email', models.EmailField(blank=True, db_column='email_contact', max_length=254, null=True)),
                ('media_email', models.EmailField(blank=True, db_column='email_media', max_length=254, null=True)),
                ('donation_url', models.URLField(blank=True, db_column='url_donation', null=True)),
                ('twitter_url', models.URLField(blank=True, db_column='url_twitter', null=True)),
                ('facebook_url', models.URLField(blank=True, db_column='url_facebook', null=True)),
                ('instagram_url', models.URLField(blank=True, db_column='url_instagram', null=True)),
                ('youtube_url', models.URLField(blank=True, db_column='url_youtube', null=True)),
                ('vimeo_url', models.URLField(blank=True, db_column='url_vimeo', null=True)),
                ('action_network_api_key', encrypted_model_fields.fields.EncryptedCharField(blank=True, db_column='api_key_action_network', null=True)),
                ('election_position', wagtail.fields.StreamField([('representative', wagtail.blocks.StructBlock([('body', wagtail.blocks.CharBlock(label='Body', required=True)), ('seat', wagtail.blocks.CharBlock(label='Seat', required=True))]))], blank=True, db_column='election_position', null=True)),
                ('important_dates', wagtail.fields.StreamField([('important_date', wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock(label='Date', required=True)), ('title', wagtail.blocks.CharBlock(label='Title', required=True))]))], blank=True, db_column='dates_important', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prefix', models.CharField(blank=True, db_column='name_prefix', max_length=100, null=True)),
                ('first_name', models.CharField(db_column='name_first', max_length=100)),
                ('middle_name', models.CharField(blank=True, db_column='name_middle', max_length=100, null=True)),
                ('last_name', models.CharField(db_column='name_last', max_length=100)),
                ('name_suffix', models.CharField(blank=True, db_column='name_suffix', max_length=100, null=True)),
                ('bio_statement', models.TextField(blank=True, db_column='statement_bio', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('coderedpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coderedcms.coderedpage')),
                ('body', wagtail.fields.StreamField([('row', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False)), ('column_breakpoint', wagtail.blocks.ChoiceBlock(choices=[('', 'Always expanded'), ('sm', 'sm - Expand on small screens (phone, 576px) and larger'), ('md', 'md - Expand on medium screens (tablet, 768px) and larger'), ('lg', 'lg - Expand on large screens (laptop, 992px) and larger'), ('xl', 'xl - Expand on extra large screens (wide monitor, 1200px)')], help_text='Screen size at which the column will expand horizontally or stack vertically.', required=False, verbose_name='Column Breakpoint'))])), ('column_size', wagtail.blocks.ChoiceBlock(choices=[('', 'Automatically size'), ('12', 'Full row'), ('6', 'Half - 1/2 column'), ('4', 'Thirds - 1/3 column'), ('8', 'Thirds - 2/3 column'), ('3', 'Quarters - 1/4 column'), ('9', 'Quarters - 3/4 column'), ('2', 'Sixths - 1/6 column'), ('10', 'Sixths - 5/6 column'), ('1', 'Twelfths - 1/12 column'), ('5', 'Twelfths - 5/12 column'), ('7', 'Twelfths - 7/12 column'), ('11', 'Twelfths - 11/12 column')], label='Column size', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card')), ('candidate_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True))], icon='user', label='Candidate Card')), ('reusable_content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('content', wagtail.snippets.blocks.SnippetChooserBlock('coderedcms.ReusableContent'))])), ('rich_text', wagtail.blocks.RichTextBlock(icon='code', label='Rich Text')), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], label='Content'))]))], label='Content'))])), ('cardgrid', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default'), ('coderedcms/blocks/cardgrid_group.html', 'Card group - attached cards of equal size'), ('coderedcms/blocks/cardgrid_deck.html', 'Card deck - separate cards of equal size'), ('coderedcms/blocks/cardgrid_columns.html', 'Card masonry - fluid brick pattern')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card'))], label='Content'))])), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Home Page',
            },
            bases=(sharethetrail.models.pages.CampaignSitePageMixin, 'coderedcms.coderedpage'),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=250)),
                ('summary', models.TextField(blank=True, db_column='summary', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('coderedpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coderedcms.coderedpage')),
                ('body', wagtail.fields.StreamField([('row', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False)), ('column_breakpoint', wagtail.blocks.ChoiceBlock(choices=[('', 'Always expanded'), ('sm', 'sm - Expand on small screens (phone, 576px) and larger'), ('md', 'md - Expand on medium screens (tablet, 768px) and larger'), ('lg', 'lg - Expand on large screens (laptop, 992px) and larger'), ('xl', 'xl - Expand on extra large screens (wide monitor, 1200px)')], help_text='Screen size at which the column will expand horizontally or stack vertically.', required=False, verbose_name='Column Breakpoint'))])), ('column_size', wagtail.blocks.ChoiceBlock(choices=[('', 'Automatically size'), ('12', 'Full row'), ('6', 'Half - 1/2 column'), ('4', 'Thirds - 1/3 column'), ('8', 'Thirds - 2/3 column'), ('3', 'Quarters - 1/4 column'), ('9', 'Quarters - 3/4 column'), ('2', 'Sixths - 1/6 column'), ('10', 'Sixths - 5/6 column'), ('1', 'Twelfths - 1/12 column'), ('5', 'Twelfths - 5/12 column'), ('7', 'Twelfths - 7/12 column'), ('11', 'Twelfths - 11/12 column')], label='Column size', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card')), ('candidate_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True))], icon='user', label='Candidate Card')), ('reusable_content', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('content', wagtail.snippets.blocks.SnippetChooserBlock('coderedcms.ReusableContent'))])), ('rich_text', wagtail.blocks.RichTextBlock(icon='code', label='Rich Text')), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], label='Content'))]))], label='Content'))])), ('cardgrid', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default'), ('coderedcms/blocks/cardgrid_group.html', 'Card group - attached cards of equal size'), ('coderedcms/blocks/cardgrid_deck.html', 'Card deck - separate cards of equal size'), ('coderedcms/blocks/cardgrid_columns.html', 'Card masonry - fluid brick pattern')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('fluid', wagtail.blocks.BooleanBlock(label='Full width', required=False)), ('content', wagtail.blocks.StreamBlock([('election_info_card', wagtail.blocks.StructBlock([('show_position', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True)), ('show_important_dates', wagtail.blocks.BooleanBlock(label='Show Position Information', required=True))], icon='pick', label='Election Information Card')), ('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True))], icon='image', label='Image Card')), ('image_page_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))], icon='image', label='Image Page Link Card')), ('image_url_link_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('url', wagtail.blocks.URLBlock(label='URL', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))], icon='image', label='Image URL Link Card')), ('issue_flip_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('statement', wagtail.blocks.RichTextBlock(label='Statement', required=True)), ('color', wagtail.blocks.CharBlock(label='Color', required=True)), ('front_image', wagtail.images.blocks.ImageChooserBlock(label='Front Image', required=True)), ('back_image', wagtail.images.blocks.ImageChooserBlock(label='Back Image', required=False))], icon='list-ul', label='Issue Flip Card'))], label='Content'))])), ('html', wagtail.blocks.RawHTMLBlock(form_classname='monospace', icon='code', label='HTML'))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Web Page',
            },
            bases=(sharethetrail.models.pages.CampaignSitePageMixin, 'coderedcms.coderedpage'),
        ),
        migrations.CreateModel(
            name='CampaignSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('paid_for_by', models.CharField(blank=True, db_column='paid_for_by', max_length=100, null=True)),
                ('theme', models.CharField(blank=True, db_column='site_theme', max_length=100, null=True)),
                ('title', models.CharField(blank=True, db_column='site_title', max_length=100, null=True)),
                ('top_nav_links', wagtail.fields.StreamField([('page_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))])), ('url_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('url', wagtail.blocks.URLBlock(label='Link', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))]))], blank=True, db_column='links_top_nav', null=True)),
                ('footer_links', wagtail.fields.StreamField([('page_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='Page', required=True))])), ('url_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='title', required=True)), ('url', wagtail.blocks.URLBlock(label='Link', required=True)), ('is_external_link', wagtail.blocks.BooleanBlock(label='Is External', required=False))]))], blank=True, db_column='links_footer', null=True)),
                ('campaign', models.ForeignKey(db_column='campaign', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sharethetrail.campaign')),
                ('fav_icon', models.ForeignKey(blank=True, db_column='fav_icon', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('sites', modelcluster.fields.ParentalManyToManyField(related_name='campaign_sites', to='wagtailcore.site')),
                ('top_nav_logo', models.ForeignKey(blank=True, db_column='logo_top_nav', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_column='title', max_length=250, null=True)),
                ('summary_statement', models.TextField(blank=True, db_column='statement_summary', null=True)),
                ('full_statement', models.TextField(blank=True, db_column='statement_full', null=True)),
                ('campaign', models.ForeignKey(db_column='campaign', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sharethetrail.campaign')),
                ('issue', models.ForeignKey(db_column='issue', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sharethetrail.issue')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='candidate',
            field=models.ForeignKey(blank=True, db_column='candidate', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sharethetrail.candidate'),
        ),
    ]
