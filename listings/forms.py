from django.forms import ModelForm
from .models import Listing, Report, FullReport
from django import forms
from django.utils.translation import gettext_lazy as _


# Create the form class.
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        # fields = []


class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = '__all__'
        fields = ['realtor', ]


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        # fields = '__all__'
        fields = ['listing', 'file']


# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = Listing
#         # fields = '__all__'
#         fields = ['file']

# class UploadFileForm(forms.ModelForm):
#     file = forms.FileField()

class UploadReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['date_created', 'file']


class FullReportForm(forms.ModelForm):
    class Meta:
        model = FullReport
        # fields = '__all__'
        fields = ['comments']
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }



# class UploadReportForm(ListingForm):
#     #extending form
#     # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     class Meta(ListingForm.Meta):
#         fields = ListingForm.Meta.fields
#         # fields = '__all__ file',
#         fields = ['date_created', 'file']

# class FileForm(forms.ModelForm):
#     # extending form
#     # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     class Meta:
#         model = File
#         # fields = ListingForm.Meta.fields
#         # fields = '__all__'
#         fields = ['date_created', 'file']
