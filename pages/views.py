from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.my_functions import update_next_check, update_date_appearance
from realtors.models import Realtor
import datetime
from datetime import timedelta
from listings.choices import units_choices, blocks_choices


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