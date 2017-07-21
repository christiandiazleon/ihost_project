from django import forms
from .models import ResearchGroups

'''
class ScholarshipForm(forms.ModelForm):
    title = "Scholarships"

    class Meta:
        model = Scholarship
        fields = ('name', 'description', 'who_can_apply',
             'application_process', 'terms_and_conditions',)
'''


class ResearchGroupsForm(forms.ModelForm):
    title = "Research Groups"

    class Meta:
        model = ResearchGroups
        fields = ('name', 'description',)
