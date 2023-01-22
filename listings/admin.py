from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'is_active', 'description', 'type', 'special_type', 'last_checked',
                    'next_check', 'realtor',)
    list_display_links = ('id', 'tag')
    list_filter = ('realtor',)
    list_editable = ('is_active',)
    search_fields = ('tag', 'description', 'unit', 'last_checked', 'next_checked',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)