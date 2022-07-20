from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from .models import Campaign, CampaignSite, CampaignIssue, Candidate, Issue


class CampaignAdmin(ModelAdmin):
    model = Campaign
    menu_label = 'Campaigns'
    menu_icon = 'pick'
    menu_order = 1
    exclude_from_explorer = False
    list_display = ('name', 'campaign_type',)
    list_filter = ('name', 'campaign_type',)
    search_fields = ('name', 'campaign_type',)


class CampaignSiteAdmin(ModelAdmin):
    model = CampaignSite
    menu_label = 'Campaign Sites'
    menu_icon = 'site'
    menu_order = 2
    exclude_from_explorer = False
    list_display = ('campaign',)
    list_filter = ('campaign',)
    search_fields = ('campaign',)


class CampaignIssueAdmin(ModelAdmin):
    model = CampaignIssue
    menu_label = 'Campaign Issues'
    menu_icon = 'list-ul'
    menu_order = 3
    exclude_from_explorer = False
    list_display = ('campaign', 'issue',)
    list_filter = ('campaign', 'issue',)
    search_fields = ('campaign', 'issue',)


class CandidateAdmin(ModelAdmin):
    model = Candidate
    menu_label = 'Candidates'
    menu_icon = 'user'
    menu_order = 4
    exclude_from_explorer = False
    list_display = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)


class IssueAdmin(ModelAdmin):
    model = Issue
    menu_label = 'Issues'
    menu_icon = 'list-ul'
    menu_order = 5
    exclude_from_explorer = False
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class ShareTheTrailAdminGroup(ModelAdminGroup):
    menu_label = 'Share the Trail'
    menu_icon = 'cogs'
    menu_order = 1
    items = (CampaignAdmin, CampaignSiteAdmin, CampaignIssueAdmin, CandidateAdmin, IssueAdmin)


modeladmin_register(ShareTheTrailAdminGroup)
