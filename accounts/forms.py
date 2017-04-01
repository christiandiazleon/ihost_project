from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple
from django import forms
from .models import StudentProfile, User, ProfessorProfile


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class UserCreateForm(UserCreationForm):
    '''
    speak_languages = forms.MultipleChoiceField(
        label='Speak languages',
        widget=forms.CheckboxSelectMultiple(),
        choices = User.LANGUAGES_CHOICES, initial=None
    )
    '''

    class Meta:
        fields = ("username", "email", "password1", "password2", "is_student")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["username"].label='Display name'
        self.fields["email"].label = "Email address"


class UserUpdateForm(forms.ModelForm):
    speak_languages = forms.MultipleChoiceField(
        required=False,
        label='Speak languages',
        widget=CheckboxSelectMultiple(),
        choices=User.LANGUAGES_CHOICES,
    )
    bio = forms.CharField(widget=forms.Textarea)


    # date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        widgets = {
            'gender':forms.RadioSelect,
        }
        fields = ("first_name", "last_name", "display_name", "gender",
            "country_of_origin", "speak_languages", "phone_number",
            "address", "bio", "avatar", "date_of_birth", "is_student",
            "is_professor", "is_executive",)
        model = get_user_model()


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('origin_education_school', 'current_education_school',
            'extra_occupation')


class ProfessorProfileForm(forms.ModelForm):
    occupation = forms.MultipleChoiceField(
        required=False,
        label='Occupation',
        widget=CheckboxSelectMultiple(),
        choices=ProfessorProfile.OCCUPATION_CHOICES
    )

    class Meta:
        model = ProfessorProfile
        fields = ('occupation',)
