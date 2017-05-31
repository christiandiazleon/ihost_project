from __future__ import unicode_literals
from django.contrib import admin
from .models import (SpeakLanguages, EntertainmentActivities,
    FeaturesAmenities, LodgingServiceOffer, RoomInformation)

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
