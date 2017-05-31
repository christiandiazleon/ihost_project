from __future__ import unicode_literals
from django.db import models

class SpeakLanguages(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Speak Language"
        verbose_name_plural = "Speak Languages"

    def __str__(self):
        return self.name


class EntertainmentActivities(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Entertainment Activities"
        verbose_name_plural = "Entertainment Activities"

    def __str__(self):
        return self.name


class LodgingServiceOffer(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Offered Services"
        verbose_name_plural = "Offered Services"

    def __str__(self):
        return self.name


class FeaturesAmenities(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)

    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "What amenities do you offer?"
        verbose_name_plural = "What amenities do you offer?"

    def __str__(self):
        return self.name


class RoomInformation(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Room caracteristics"
        verbose_name_plural = "Room caracteristics"

    def __str__(self):
        return self.name
