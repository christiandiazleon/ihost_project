from __future__ import unicode_literals
from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, StudentProfile, ProfessorProfile
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Inherit of the original UserAdmin for use the customized forms
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'classes':('wide',),
                'fields':(
                    'slug',
                    #'first_name',
                    #'last_name',
                    'display_name',
                    'gender',
                    'country_of_origin',
                    'speak_languages',
                    #'email',
                    'phone_number',
                    'address',
                    'bio',
                    'avatar',
                    'date_of_birth',
                    'is_student',
                    'is_professor',
                    'is_executive',
                ),
            }
        ),
    )
    # exclude = ('first_name', 'last_name')

# Change our UserAdmin class to inherit of our CustomUserAdmin created above (do not inherit of model.ModelAdmin)

@admin.register(User)
class UserAdmin(CustomUserAdmin):

    list_display = ('id', 'username', 'slug','first_name', 'last_name', 'display_name','gender','country_of_origin',
        'speak_languages','phone_number','address','email',
                    'bio','date_of_birth','is_student','is_professor',
                    'is_executive', )

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'slug')

@admin.register(ProfessorProfile)
class ProfessorProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', )

