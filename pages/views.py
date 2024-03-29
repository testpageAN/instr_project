import pytz
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.my_functions import update_next_check, update_date_appearance, update_next_check_for_one
from realtors.models import Realtor
import datetime
from datetime import datetime
from datetime import timedelta
from django.utils.timezone import make_aware, get_default_timezone
from listings.choices import units_choices, blocks_choices
import pytz

import csv
import io
# from datetime import datetime
from django.shortcuts import render, redirect
from listings.models import Listing

from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def index(request):
    listings = Listing.objects.order_by('-next_check').filter(is_active=True)
    update_next_check(listings)

    due_listings = []
    for listing in listings:
        # listing.delta_days = (listing.next_check.date() - datetime.date.today()).days
        listing.delta_days = (listing.next_check.date() - datetime.today().date()).days

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
    if request.method == "POST":
        try:
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode("utf-8")
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)
            for row in reader:
                if Listing.objects.filter(tag=row["tag"]).exists():
                    messages.warning(request, f"Listing with tag {row['tag']} already exists in the database.")
                else:
                    # assuming the input string is in the format "YYYY-MM-DD HH:MM:SS+HH:MM"
                    date_str = '2022-12-31 00:00:00+02:00'
                    naive_date = datetime.strptime(date_str[:-6], '%Y-%m-%d %H:%M:%S')
                    aware_date = pytz.timezone('Africa/Cairo').localize(naive_date)

                    listing = Listing.objects.create(
                            realtor_id=row["realtor_id"],
                            tag=row["tag"],
                            block=row["block"],
                            unit=row["unit"],
                            description=row["description"],
                            type=row["type"],
                            detailed_type=row["detailed_type"],
                            special_type=row["special_type"],
                            lrv=row["lrv"],
                            urv=row["urv"],
                            units=row["units"],
                            manufacturer=row["manufacturer"],
                            model=row["model"],
                            serial_no=row["serial_no"],
                            system_type=row["system_type"],
                            equipment=row["equipment"],
                            project=row["project"],
                            interval=row["interval"],
                            # last_checked=datetime.now(),
                            # last_checked=row["last_checked"],
                            last_checked=aware_date,  # use the converted datetime object
                            # next_check=row["next_check"],
                            is_active=row["is_active"],
                            history=row["history"],
                        )
            # redirect to listings page upon successful import
            #         update_next_check_for_one(listing)
            messages.success(request, f'Listings was UPDATED')
            # listings = Listing.objects.all()
            # update_next_check(listings)
            # context = {
            #     "listings": listings,
            # }
            return redirect("listings")
            # return render(request, "listings/listings.html", context)
        except Exception as e:
            messages.error(request, f"An error occurred while importing data: {e}")
    return render(request, "pages/import-data.html")


# def import_data(request):
#     if request.method == "POST":
#         try:
#             csv_file = request.FILES["csv_file"]
#             decoded_file = csv_file.read().decode("utf-8")
#             io_string = io.StringIO(decoded_file)
#             reader = csv.DictReader(io_string)
#             for row in reader:
#                 try:
#                     listing = Listing.objects.get(tag=row["tag"])
#                     # Listing already exists, skip this row
#                     continue
#                 except ObjectDoesNotExist:
#                     # Listing doesn't exist, create a new one
#                     listing = Listing.objects.create(
#                         realtor_id=row["realtor_id"],
#                         tag=row["tag"],
#                         block=row["block"],
#                         unit=row["unit"],
#                         description=row["description"],
#                         type=row["type"],
#                         detailed_type=row["detailed_type"],
#                         special_type=row["special_type"],
#                         lrv=row["lrv"],
#                         urv=row["urv"],
#                         units=row["units"],
#                         manufacturer=row["manufacturer"],
#                         model=row["model"],
#                         serial_no=row["serial_no"],
#                         system_type=row["system_type"],
#                         equipment=row["equipment"],
#                         project=row["project"],
#                         interval=row["interval"],
#                         # last_checked=datetime.now(),
#                         last_checked=row["last_checked"],
#                         next_check=row["next_check"],
#                         is_active=row["is_active"],
#                         history=row["history"],
#                     )
#                 # return redirect('listings')
#         except Exception as e:
#             # Handle any type of error
#             return render(request, "pages/import-data.html", {"error": str(e)})
#     return render(request, "pages/import-data.html")


# def import_data(request):
#     if request.method == "POST":
#         csv_file = request.FILES["csv_file"]
#         decoded_file = csv_file.read().decode("utf-8")
#         io_string = io.StringIO(decoded_file)
#         reader = csv.DictReader(io_string)
#         for row in reader:
#             listing = Listing.objects.create(
#                 realtor_id=row["realtor_id"],
#                 tag=row["tag"],
#                 block=row["block"],
#                 unit=row["unit"],
#                 description=row["description"],
#                 type=row["type"],
#                 detailed_type=row["detailed_type"],
#                 special_type=row["special_type"],
#                 lrv=row["lrv"],
#                 urv=row["urv"],
#                 units=row["units"],
#                 manufacturer=row["manufacturer"],
#                 model=row["model"],
#                 serial_no=row["serial_no"],
#                 system_type=row["system_type"],
#                 equipment=row["equipment"],
#                 project=row["project"],
#                 interval=row["interval"],
#                 # last_checked=datetime.now(),
#                 last_checked =row["last_checked"],
#                 next_check=row["next_check"],
#                 is_active=row["is_active"],
#                 history=row["history"],
#             )
#     return render(request, "pages/import-data.html")
