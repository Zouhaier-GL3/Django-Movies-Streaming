from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from import_export.admin import ImportExportModelAdmin

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'category', 'streaming', 'server','trailer','description', 'year','image')
    list_display_links = ('id','title')
    list_editable = ('description',)
    list_per_page = 10
    search_fields = ('title', 'category', 'streaming', 'server','trailer','description', 'year','image')
    list_filter = ('category', 'date_added')


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
