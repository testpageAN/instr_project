from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.my_functions import update_next_check, update_date_appearance
from realtors.models import Realtor
import datetime
from datetime import timedelta
from listings.choices import units_choices, blocks_choices


import csv
# from datetime import datetime
from django.shortcuts import render
from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by('-next_check').filter(is_active=True)
    update_next_check(listings)

    due_listings = []
    for listing in listings:
        listing.delta_days = (listing.next_check.date() - datetime.date.today()).days
        if 0 <= listing.delta_days <= 30:
            due_listings.append(listing)
            print(listing.next_check)

    update_date_appearance(due_listings)

    context = {
        'due_listings': due_listings,
        'units_choices': units_choices,
        'blocks_choices': blocks_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors
    }
    return render(request, 'pages/about.html', context)


def import_data(request):
    # if request.method == "POST":
    #     csv_file = request.FILES["csv_file"]
    #     decoded_file = csv_file.read().decode("utf-8")
    #     io_string = io.StringIO(decoded_file)
    #     reader = csv.DictReader(io_string)
    #     for row in reader:
    #         listing = Listing.objects.create(
    #             realtor_id=row["realtor_id"],
    #             tag=row["tag"],
    #             block=row["block"],
    #             unit=row["unit"],
    #             description=row["description"],
    #             type=row["type"],
    #             detailed_type=row["detailed_type"],
    #             special_type=row["special_type"],
    #             lrv=row["lrv"],
    #             urv=row["urv"],
    #             units=row["units"],
    #             manufacturer=row["manufacturer"],
    #             model=row["model"],
    #             serial_no=row["serial_no"],
    #             system_type=row["system_type"],
    #             equipment=row["equipment"],
    #             project=row["project"],
    #             interval=row["interval"],
    #             last_checked=datetime.now(),
    #             next_check=row["next_check"],
    #             is_active=row["is_active"],
    #             history=row["history"],
    #         )
    return render(request, "pages/import-data.html")
