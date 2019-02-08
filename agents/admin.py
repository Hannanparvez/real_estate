from django.contrib import admin
from .models import Agent


class AgentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','is_mvp','is_team')
    list_editable=('is_mvp','is_team',)
    list_display_links=('id','name')
    search_fields=('name',)
    list_per_page=25

admin.site.register(Agent,AgentAdmin)



