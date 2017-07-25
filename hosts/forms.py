from django import forms
from .models import LodgingOffer, StudiesOffert
from django_countries.widgets import CountrySelectWidget


class StudiesOffertForm(forms.ModelForm):
    #user = self.request.user
    title = "Studies Offert"
    #scholarships = forms.ModelForm(queryset=Scholarship.objects.filter(created_by__username=user))

    class Meta:
        model = StudiesOffert
        fields = ('ad_title', 'country', 'city',
            'institute_character', 'students_number', 'knowledge_topics',
            'duration', 'studies_type_offered', 'academic_mobility_programs',
            'additional_description', 'photo',)
        # exclude = ('hosting_host_user',)
        # to put after: 'accreditations'

class DateInput(forms.DateInput):
    input_type = 'date'

class LodgingOfferForm(forms.ModelForm):
    title = "Create Lodging Offert"
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=LodgingOffer.BIRTH_YEAR_CHOICES))

    class Meta:
        widgets = {
            # 'available_dates': forms.DateInput(attrs={'class':'datepicker'}),
            'available_dates': forms.DateInput(attrs={'class':'datepicker'}),
            'country': CountrySelectWidget(),
        }
        model = LodgingOffer
        fields = ('ad_title', 'country', 'city', 'address', 'lodging_offer_type', 'stars', 'available_dates', 'offered_services',
            'featured_amenities', 'room_type_offered',
            'number_guest_room_type', 'bed_type', 'bathroom',
            'room_information', 'photographies', 'room_value',
            'additional_description',)

        # exclude = ('hosting_host_user',)


class LodgingOfferSearchForm(forms.Form):
    query = forms.CharField(label='')


class StudiesOffertSearchForm(forms.Form):
    query = forms.CharField(label='')

