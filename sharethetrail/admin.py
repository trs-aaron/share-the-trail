from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from .models import Campaign


class CampaignAdmin(ModelAdmin):
    model = Campaign
    menu_label = "Campaigns"
    menu_icon = "pick"
    menu_order = 200
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("first_name", "last_name",)
    list_filter = ("first_name", "last_name",)
    search_fields = ("first_name", "last_name",)


modeladmin_register(CampaignAdmin)
