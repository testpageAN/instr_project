from django.contrib import admin
# from .models import Listing, File
from .models import Listing, Report, FullReport


# Register your models here.

class ReportAdmin(admin.ModelAdmin):

    list_display = ('id', 'listing', 'name', 'date_created', 'file')
    list_display_links = ('id', 'listing', 'name')
    search_fields = ()
    list_per_page = 25


class FullReportAdmin(admin.ModelAdmin):

    list_display = ('id', 'listing', 'name', 'date_created', 'file')
    list_display_links = ('id', 'listing', 'name')
    search_fields = ()
    list_per_page = 25


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'is_active', 'description', 'type', 'special_type', 'last_checked',
                    'next_check', 'realtor',)# 'foreignkey.file')
    list_display_links = ('id', 'tag')
    list_filter = ('realtor',)
    list_editable = ('is_active',)
    search_fields = ('tag', 'description', 'unit', 'last_checked', 'next_checked',)
    list_per_page = 25


# class FileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'date_created', 'file', 'listing')
#     list_display_links = ('id', 'name')


admin.site.register(Listing, ListingAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(FullReport, FullReportAdmin)
# admin.site.register(File, FileAdmin)
