from django.shortcuts import render, get_object_or_404
import os

from django.utils.html import linebreaks

from .models import Listing
import datetime
from datetime import timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .my_functions import update_next_check, update_last_checked
from django.views.generic.detail import DetailView
from .choices import units_choices, blocks_choices, control_users

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .forms import ListingForm, PostFileForm
# from .forms import ListingForm, FileForm
from .forms import ListingForm, UploadReportForm, ReportForm, CreateReportForm
from .models import Report

from django.contrib import messages, auth

from django.contrib.auth.models import User

from openpyxl import Workbook


#Create your views here.
# class ListingView(LoginRequiredMixin, View):
#     def get(self, request):
#         listings = Listing.objects.all()
#         context = {'listings': listings}
#         return render(request, 'listings/listings.html', context)


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

    fields = Listing._meta.get_fields()
    reports = Report.objects.all().filter(listing_id=listing_id)

    context = {
        'listing': listing,
        'reports': reports,
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

#################################################################################
def edit(request, listing_id):
    context = {}
    # fetch the object related to passed id
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
        'listing': listing,
    }
    form = ListingForm(request.POST or None, instance=listing)
    # save the data from the form and redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, f'{listing} was UPDATED')
        # return redirect("listing")
        return render(request, "listings/listing.html", context)

    # add form dictionary to context
    context["form"] = form

    # return render(request, 'listings/listing.html', context)
    return render(request, "listings/edit.html", context)

############################################################################################################


def insert(request):
    # dictionary for initial data with field names as keys
    context = {}

    # add the dictionary during initialization
    form = ListingForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            form.save()
            messages.success(request, f"{Listing.objects.filter().order_by('id').last()} was CREATED SUCCESSFULLY")
            return redirect("listings")
        else:
            messages.error(request, "Listing was NOT created. LOOK FOR PROBLEMS")
            return redirect("listings")

    context['form'] = form
    return render(request, "listings/insert.html", context)


############################################################################################################

# class ListingDeleteView(DeleteView):
#     # looks for model_confirm_delete.html
#     model = Listing
#     success_url = reverse_lazy('listings')


def remove(request, listing_id):

    # fetch the object related to passed id
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
        'listing': listing,
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.username in control_users:
                print(request.user.username in control_users)
                # delete object
                listing.delete()
                # after deleting redirect to listings page
                messages.success(request, f'{listing} was deleted')
                return redirect("listings")
            else:
                messages.error(request, f'No credentials for deleting {listing}')
                return redirect("listings")

    return render(request, "listings/listing_confirm_delete.html", context)

###################################################################################################
####################################################################################################
###################################################################################################
####################################################################################################
#################################################################################################

    # return render(request, 'listings/create-report.html',)
###################################################################################################
####################################################################################################
###################################################################################################
####################################################################################################
 ###################################################################################################
####################################################################################################
def upload_report(request, listing_id):
    # context = {}
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
            'listing': listing,
        }
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            update_last_checked(listing)
            listing.save()
            form.save()
            messages.success(request, f'{listing} was UPDATED')
            # return redirect('listings')
            return redirect('listing', listing_id)
            # return render(request, 'listings/listing.html', context)
    else:
        form = ReportForm()
        context = {
            'listing': listing,
            'form': form,
        }

    return render(request, 'listings/upload-report.html', context)


#######################################################################################################
## λειτουργει χωρις το upload του file
##
#######################################################################################################
# def create_report(request, listing_id):
#     listing = get_object_or_404(Listing, id=listing_id)
#     context = {
#         'listing': listing,
#     }
#     old_history = listing.history
#     form = CreateReportForm(request.POST or None, instance=listing)
#     if request.method == 'POST':
#         if form.is_valid():
#             new_history = request.POST.get('history')
#             listing.history = old_history + '\n\n' + new_history
#             wb = Workbook()
#             ws = wb.active
#             ws['A4'] = listing.tag
#             ws['A6'] = listing.history
#             wb.save('my_first_report6.xlsx')
#             #file = 'my_first_report6.xlsx'
#             update_last_checked(listing)
#             listing.save()
#             # form.save()
#             # messages.success(request, f'{listing} report was created')
#             messages.success(request, f'{listing} report was created')
#             return redirect('listings')
#             # return render(request, 'listings/listing.html', context)
#     else:
#         form = CreateReportForm()
#         context = {
#             'listing': listing,
#             'form': form,
#         }
#
#     return render(request, 'listings/create-report.html', context)

##########################################################################################################
##    TEST
##########################################################################################################
def create_report(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
        'listing': listing,
    }
    old_history = listing.history
    form = CreateReportForm(request.POST or None, instance=listing)
    if request.method == 'POST':
        if form.is_valid():
            new_history = request.POST.get('history')
            listing.history = old_history + '\n\n' + new_history
            wb = Workbook()
            ws = wb.active
            ws['A4'] = listing.tag
            ws['A6'] = listing.history
            wb.save('my_first_report16.xlsx')
            file = 'my_first_report16.xlsx'
            update_last_checked(listing)
            listing.save()
            new_report = Report(listing=listing, file=file)
            new_report.save()
            context = {
                'listing': listing,
                # 'file': file,
                # 'new_report': new_report,
            }
            messages.success(request, f'{listing} report was created and uploaded!!!')
            # return redirect('listings')
            return redirect('listing', listing_id)
            # return render(request, 'listings/listings.html', context)

    else:
        form = CreateReportForm()
        context = {
            'listing': listing,
            'form': form,
        }
    return render(request, 'listings/create-report.html', context)




########################################################################################################

#https://stackoverflow.com/questions/57183002/filefield-not-working-with-arrayfield-in-django
#https://code.djangoproject.com/attachment/ticket/25756/multiple.py

################################################################################################################


