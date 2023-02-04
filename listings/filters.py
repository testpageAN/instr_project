import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter, ChoiceFilter

from django_filters.views import FilterView
# from django_tables2.views import SingleTableMixin

from .models import *
from accounts.models import *
from pages.models import *
from .tables import ListingTable


# def get_unit():
#     unit = ((), ())
#     for listing in Listing.objects.all():
#         unit[0] += tuple(str(listing.unit))
#         unit[1] += tuple(str(listing.unit))
#     return unit
#
#
# x = get_unit()
# print(x)

units = (
    (100, 100),
    ('1100', '1100'),
    ('1500', 1500),
    (92500, 92500),
)


class ListingFilter(django_filters.FilterSet):
    start_date_1 = DateFilter(field_name='last_checked', lookup_expr='gte', label="Last Check from")
    end_date_1 = DateFilter(field_name='last_checked', lookup_expr='lte', label="Last Check to")
    start_date = DateFilter(field_name='next_check', lookup_expr='gte', label="Next Check from")
    end_date = DateFilter(field_name='next_check', lookup_expr='lte', label='Next Check to')
    type = CharFilter(field_name='type', lookup_expr='icontains', label='Type')
    special_type = CharFilter(field_name='special_type', lookup_expr='icontains', label='Special Type')
    # unit = CharFilter(field_name='unit', lookup_expr='exact', label='Unit')
    # unit = ChoiceFilter(field_name='unit', lookup_expr='iexact', label='Unit', choices=get_unit())
    unit = ChoiceFilter(field_name='unit', lookup_expr='iexact', label='Unit', choices=units)
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

# class ListingFilter(django_filters.FilterSet):
#     unit = NumberFilter(method='my_custom_filter')
#
#     class Meta:
#         model = Listing
#         fields = ['unit']
#         # fields = {'unit': ['exact']}
#
#     def my_custom_filter(self, queryset, unit, value):
#         return queryset.filter(**{
#             unit: value,
#         })


# class F(django_filters.FilterSet):
#     username = CharFilter(method='my_custom_filter')
#
#     class Meta:
#         model = User
#         fields = ['username']
#
#     def my_custom_filter(self, queryset, name, value):
#         return queryset.filter(**{
#             name: value,
#         })
