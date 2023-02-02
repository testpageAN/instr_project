import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *
from accounts.models import *
from pages.models import *


class ListingFilter(django_filters.FilterSet):
    start_date_1 = DateFilter(field_name='last_checked', lookup_expr='gte', label="Last Check from")
    end_date_1 = DateFilter(field_name='last_checked', lookup_expr='lte', label="Last Check to")
    start_date = DateFilter(field_name='next_check', lookup_expr='gte', label="Next Check from")
    end_date = DateFilter(field_name='next_check', lookup_expr='lte', label='Next Check to')
    type = CharFilter(field_name='type', lookup_expr='icontains', label='Type')
    special_type = CharFilter(field_name='special_type', lookup_expr='icontains', label='Special Type')
    unit = NumberFilter(field_name='unit', lookup_expr='exact', label='Unit')
    interval = NumberFilter(field_name='interval', lookup_expr="lte", label='Interval')


    class Meta:
        model = Listing
        # fields = '__all__'
        fields = ['unit', 'type', 'special_type', 'units', 'last_checked', 'interval', 'next_check']
        exclude = ['last_checked', 'next_check']
        # labels = {
        #     'last_checked': ('Last Checked'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }


