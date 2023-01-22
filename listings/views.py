from django.shortcuts import render, get_object_or_404
from .models import Listing
import datetime
from datetime import timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .my_functions import update_next_check
from django.views.generic.detail import DetailView
from .choices import units_choices, blocks_choices

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    # listings = Listing.objects.order_by('unit')
    listings = Listing.objects.order_by('tag')
    update_next_check(listings)

    paginator = Paginator(listings, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,

    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    # all_fields = Listing._meta.get_fields()

    context = {
        'listing': listing,
        # 'all_fields': all_fields,
    }

    return render(request, 'listings/listing.html', context)

# class SingleListingView(DetailView):
#     template_name = 'listings/listing.html'
#     model = Listing


def search(request):

    queryset_list = Listing.objects.order_by('tag')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(tag__icontains=keywords)

    # Block
    if 'block' in request.GET:
        block = request.GET['block']
        if block:
            queryset_list = queryset_list.filter(block__iexact=block)

    # Unit
    if 'unit' in request.GET:
        unit = request.GET['unit']
        if unit:
            queryset_list = queryset_list.filter(unit__iexact=unit)

    # # Realtor
    # if 'realtor' in request.GET:
    #     realtor = request.GET['realtor']
    #     if realtor:
    #         queryset_list = queryset_list.filter(realtor__name__iexact=realtor)

    context = {
        'units_choices': units_choices,
        'blocks_choices': blocks_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


def edit(request, listing_id):
    return render(request, 'listings/edit.html',)


def insert(request):
    return render(request, 'listings/insert.html',)


def remove(request, listing_id):
    return render(request, 'listings/remove.html',)


def create_report(request, listing_id):
    return render(request, 'listings/create-report.html',)
