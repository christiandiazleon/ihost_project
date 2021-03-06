from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple
from django import forms
from .models import (StudentProfile, ProfessorProfile, ExecutiveProfile,
                    StudyHostProfile, HostingHostProfile)

from django_countries.widgets import CountrySelectWidget


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)


class UserCreateForm(UserCreationForm):

    class Meta:
        widgets = {
            # 'user_type':forms.RadioSelect(attrs={'id': 'r1_0', 'id':'r1_1'}),
            'user_type':forms.RadioSelect(),
            #'user_type':forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':'r1_0'}))
        }

        fields = ("email", "password1", "password2", "user_type",)
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = "Email address"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Password confirmation"





class DateInput(forms.DateInput):
    input_type = 'date'


class UserUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        widgets = {
            # 'gender':forms.RadioSelect,
            'country_of_origin': CountrySelectWidget(),
            'country_current_residence': CountrySelectWidget(),
            # I can customize these https://github.com/SmileyChris/
            # django-countries#countryselectwidget
             'date_of_birth': DateInput(), #datepicker
            #'date_of_birth': forms.DateInput(attrs={'class':'datepicker'})
        }

        fields = ("first_name", "last_name", "gender", "enterprise_name",
        "country_of_origin", "city_of_origin", "country_current_residence",
        "city_current_residence", 'speak_languages', "phone_number",
        "address", "bio", "avatar", "date_of_birth",
        'entertainment_activities', "is_student", "is_professor",
        "is_executive", "is_study_host", "is_hosting_host",)

        model = get_user_model()


class UserEnterpriseUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        widgets = {
            'gender':forms.RadioSelect,
            'country_of_origin': CountrySelectWidget(),
            'country_current_residence': CountrySelectWidget(),
            # I can customize these https://github.com/SmileyChris/
            # django-countries#countryselectwidget
            'date_of_birth': DateInput(), #datepicker
        }
        fields = ("enterprise_name", "country_of_origin", "city_of_origin", "country_current_residence", "city_current_residence",
            "phone_number", "address", "bio", "avatar", "date_of_birth",
            "is_study_host", "is_hosting_host",)

        model = get_user_model()

class StudentProfileForm(forms.ModelForm):
    title = "Student Details"

    class Meta:
        model = StudentProfile
        fields = ('origin_education_school', 'current_education_school',
                  'extra_occupation', 'educational_titles',
                  'complete_studies_school', 'knowledge_topics_choice',)


class ProfessorProfileForm(forms.ModelForm):
    title = "Professor Details"
    occupation = forms.MultipleChoiceField(
        required=False,
        label='Occupation',
        widget=CheckboxSelectMultiple(),
        choices=ProfessorProfile.OCCUPATION_CHOICES
    )
    research_groups = forms.CharField(widget=forms.Textarea)
    autorship_publications = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ProfessorProfile
        fields = ('occupation', 'origin_education_school',
            'current_education_school', 'educational_titles',
            'complete_studies_school', 'knowledge_topics_choice',
            'research_groups', 'autorship_publications',)


class ExecutiveProfileForm(forms.ModelForm):
    title = "Executive Details"
    # companies_to_visit = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ExecutiveProfile
        fields = ('enterprise_name',
        'educational_titles', 'complete_studies_school',
        'innovation_topics_choice', )


class StudyHostProfileForm(forms.ModelForm):
    title = "Study Host Details"
    widgets = {
            'institute_character':forms.RadioSelect,
    }

    high_quality_accreditations = forms.MultipleChoiceField(
        required=False,
        label='Accreditations of high quality',
        widget=CheckboxSelectMultiple(),
        choices=StudyHostProfile.ACCREDITATIONS_CHOICES,
    )

    rankings_classification = forms.CharField(widget=forms.Textarea)
    #knowledge_topics_choice = forms.CharField(widget=forms.Textarea)
    strengths = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = StudyHostProfile
        fields = ('institution_type', 'institute_character',
            'high_quality_accreditations', 'students_number',
            'rankings_classification', 'knowledge_topics',
            'strengths', 'photography')
        #exclude = ('studies_offert_list', )


class HostingHostProfileForm(forms.ModelForm):
    title = "Hosting Host Details"

    class Meta:
        model = HostingHostProfile
        fields = ('lodging_offer_type', 'featured_amenities', 'stars',
            'photography', 'additional_description')
