from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django import forms
from .models import StudentProfile, User


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


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('origin_education_school', 'current_education_school',
            'extra_occupation')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        speak_languages = forms.MultipleChoiceField(
            label='Speak languages',
            widget=forms.CheckboxSelectMultiple(),
            choices = User.LANGUAGES_CHOICES, initial=None
        )
