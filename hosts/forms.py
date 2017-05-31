from django import forms
from .models import LodgingOffer


class LodgingOfferForm(forms.ModelForm):
    title = "Creating Lodging Offert"
    additional_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = LodgingOffer
        fields = ('lodging_offer_type', 'offered_services',
            'featured_amenities', 'room_information', 'room_value',
            'additional_description')
        exclude = ('hosting_host_user',)


class HostingOfferSearchForm(forms.ModelForm):
    query = forms.CharField(label='')

