from django import forms
from .models import LodgingOffer


class LodgingOfferForm(forms.ModelForm):
    title = "Creating Lodging Offert"
    additional_description = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = LodgingOffer
        fields = ('hosting_host_user', 'available_dates', 'lodging_offer_type', 'offered_services', 'room_information', 'room_value',
            'additional_description')
        widgets = {
            'available_dates': forms.DateInput(attrs={'class':'datepicker'}),

        }
        # exclude = ('hosting_host_user',)


class HostingOfferSearchForm(forms.ModelForm):
    query = forms.CharField(label='')

