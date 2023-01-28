from django.forms import ModelForm
from .models import Listing, Report
from django import forms


# Create the form class.
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        # fields = []


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
