from __future__ import unicode_literals
from django.contrib import admin
from .models import (SpeakLanguages, EntertainmentActivities,
    FeaturesAmenities, LodgingServiceOffer, RoomInformation, ResearchGroups, Scholarship, LodgingOfferType)

# Register your models here.

@admin.register(SpeakLanguages)
class SpeakLanguagesAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)

@admin.register(EntertainmentActivities)
class EntertainmentActivitiesAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')


@admin.register(FeaturesAmenities)
class FeaturesAmenitiesAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')


@admin.register(LodgingServiceOffer)
class LodgingServiceOfferAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')

@admin.register(RoomInformation)
class RoomInformationAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')

@admin.register(ResearchGroups)
class ResearchGroupsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'who_can_apply', 'application_process', 'terms_and_conditions',)

@admin.register(LodgingOfferType)
class LodgingOfferTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)

