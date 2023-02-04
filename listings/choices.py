from .models import *


listings = Listing.objects.all()
units_choices = {}
sorted_keys = []
for listing in listings:
    if listing.unit not in sorted_keys:
        sorted_keys.append(listing.unit)
sorted_keys.sort()

for listing in sorted_keys:
    if listing not in units_choices.keys():
        units_choices[str(listing)] = listing

print(units_choices)


# units_choices = {
#     '100': 100,
#     '1100': 1100,
#     '200': 200,
#     '500': 500,
#     '1500': 1500,
#     '4700': 4700,
# }

sorted(units_choices.items())

realtors_choices = {
    'Tasos K': 'Tasos K',
    'Dimitris M': 'Dimitris M',
    'Gerasimos B': 'Gerasimos B',
}

blocks_choices = {
    'Lubes': 'Lubes',
    'Fuels': 'Fuels',
    'FCC': 'FCC',
}

control_users = ['alexis', ]
