from django.http import HttpResponse

from .models import *
from realtors.models import Realtor
from django.db.utils import OperationalError

# listings = Listing.objects.all()

#########################################################

from django.apps import apps
from django.db.utils import OperationalError

Listing = apps.get_model('listings', 'Listing')

try:
    listings = Listing.objects.all()
    units_choices = {}
    sorted_units_keys = []
    # if listings:
    for listing in listings:
        if listing.unit not in sorted_units_keys:
            sorted_units_keys.append(listing.unit)
    sorted_units_keys.sort()

    for listing in sorted_units_keys:
        if listing not in units_choices.keys():
            units_choices[str(listing)] = listing
except (OperationalError, LookupError):
    pass


# try:
#     listings = Listing.objects.all()
#     units_choices = {}
#     sorted_units_keys = []
#     if listings:
#         for listing in listings:
#             if listing.unit not in sorted_units_keys:
#                 sorted_units_keys.append(listing.unit)
#         sorted_units_keys.sort()
#
#     for listing in sorted_units_keys:
#         if listing not in units_choices.keys():
#             units_choices[str(listing)] = listing
# except OperationalError:
#     pass

# units_choices = {}
# sorted_units_keys = []
# # if listings:
# for listing in listings:
#     if listing.unit not in sorted_units_keys:
#         sorted_units_keys.append(listing.unit)
# sorted_units_keys.sort()
#
#
# for listing in sorted_units_keys:
#     if listing not in units_choices.keys():
#         units_choices[str(listing)] = listing

# print(units_choices)
##########################################################

intervals_choices = {}
sorted_intervals_keys = []
if listings:
    for listing in listings:
        if listing.interval not in sorted_intervals_keys:
            sorted_intervals_keys.append(listing.interval)
    sorted_intervals_keys.sort()

for listing in sorted_intervals_keys:
    if listing not in intervals_choices.keys():
        intervals_choices[str(listing)] = listing

# print(intervals_choices)
##########################################################

measure_units_choices = {}
sorted_measure_units_keys = []
if listings:
    for listing in listings:
        if listing.units not in sorted_measure_units_keys:
            sorted_measure_units_keys.append(listing.units)
    sorted_measure_units_keys.sort()

for listing in sorted_measure_units_keys:
    if listing not in measure_units_choices.keys():
        measure_units_choices[str(listing)] = listing

# print(measure_units_choices)
##########################################################

realtors_choices = {}
sorted_realtors_keys = []
if listings:
    for listing in listings:
        if listing.realtor not in sorted_realtors_keys:
            sorted_realtors_keys.append(listing.realtor)

for listing in sorted_realtors_keys:
    if listing not in realtors_choices.keys():
        realtors_choices[str(listing)] = str(listing)

# print(realtors_choices)
##########################################################

blocks_choices = {}
sorted_blocks_keys = []
if listings:
    for listing in listings:
        if listing.block not in sorted_blocks_keys:
            sorted_blocks_keys.append(listing.block)

for listing in sorted_blocks_keys:
    if listing not in blocks_choices.keys():
        blocks_choices[str(listing)] = str(listing)

# print(blocks_choices)
##########################################################

types_choices = {}
sorted_types_keys = []
if listings:
    for listing in listings:
        if listing.type not in sorted_types_keys:
            sorted_types_keys.append(listing.type)

for listing in sorted_types_keys:
    if listing not in types_choices.keys():
        types_choices[str(listing)] = str(listing)

# print(types_choices)
##########################################################

special_types_choices = {}
sorted_special_types_keys = []
if listings:
    for listing in listings:
        if listing.special_type not in sorted_special_types_keys:
            sorted_special_types_keys.append(listing.special_type)

for listing in sorted_special_types_keys:
    if listing not in special_types_choices.keys():
        special_types_choices[str(listing)] = str(listing)

# print(special_types_choices)


is_active_choices = {
    True: True,
    False: False,
}

control_users = ['alexis', ]
