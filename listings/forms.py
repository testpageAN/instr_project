from django.forms import ModelForm
from .models import Listing


# Create the form class.
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'

