#
# import django_tables2 as tables
# from django.utils.safestring import mark_safe
# from django.urls import reverse
# from django_tables2.utils import A
#
# from .models import Listing
# from .my_functions import update_next_check, update_next_check_for_one
# # from .views import Listing
#
#
# class ListingTable(tables.Table):
#     # details = tables.LinkColumn('item_edit', args=[A('pk')], orderable=False)
#     details = tables.LinkColumn('listing', args=[A('id')], orderable=True, empty_values=(), attrs={
#         "a": {"class": "btn btn-primary btn-block;"}
#     })
#     # next_check = tables.LinkColumn('listing', orderable=True, empty_values=())
#     # next_check = tables.DateColumn(short=True)
#
#     # tag = tables.Column(footer="Total:")
#     tag = tables.Column(
#         footer="Total: " + str(Listing.objects.count())
#     )
#
#     class Meta:
#         model = Listing
#         template_name = "django_tables2/bootstrap4.html"
#         fields = ('unit', 'tag', 'description', 'type', 'special_type', 'lrv', 'urv', 'units', 'is_active', 'last_checked', 'interval', 'next_check',)
#
#     # ΔΕΝ ΛΕΙΤΟΥΡΓΕΙ
#     # def render_next_check(self, pk=id):
#     #     listing = Listing.objects.filter(pk=id)
#     #     date = update_next_check_for_one(listing)
#     #     return "how to pass date?"
#     #     return date
#
#     # def render_next_check(self):
#     #     return "how to pass date?"
#
#     def render_details(self):
#         return 'DETAILS'
