from django import forms
from .models import LodgingOffer, StudiesOffert


class StudiesOffertForm(forms.ModelForm):
    title = "Creating Studies Offert"

    class Meta:
        model = StudiesOffert
        fields = ('knowledge_topics', 'studies_type_offered',
             'academic_mobility_programs', 'scholarships', 'photo',)
        # exclude = ('hosting_host_user',)


class LodgingOfferForm(forms.ModelForm):
    title = "Creating Lodging Offert"
    #birth_year = forms.DateField(widget=forms.SelectDateWidget(years=LodgingOffer.BIRTH_YEAR_CHOICES))

    class Meta:
        model = LodgingOffer
        fields = ('ad_title', 'available_dates', 'offered_services', 'room_type_offered', 'number_guest_room_type',
            'room_information', 'photographies', 'room_value',
            'additional_description',)
        widgets = {
            'available_dates': forms.DateInput(attrs={'class':'datepicker'}),


        }
        # exclude = ('hosting_host_user',)


class HostingOfferSearchForm(forms.ModelForm):
    query = forms.CharField(label='')

