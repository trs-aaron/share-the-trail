from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from .models import Campaign


class CampaignAdmin(ModelAdmin):
    model = Campaign
    menu_label = "Campaigns"
    menu_icon = "pick"
    menu_order = 100
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("site", "first_name", "last_name", "election_office",)
    list_filter = ("first_name", "last_name", "election_office",)
    search_fields = ("first_name", "last_name",)


modeladmin_register(CampaignAdmin)
