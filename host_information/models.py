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

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Room caracteristics"
        verbose_name_plural = "Room caracteristics"

    def __str__(self):
        return self.name


# Relacionarlo con el studyhost y que este pueda ingresarlos
# para despues traerlos en el campo de grupos de invest en su perfil
class ResearchGroups(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Research Groups"
        verbose_name_plural = "Research Groups"

    def __str__(self):
        return self.name

# Relacionarlo con el studyhost y que este pueda ingresarlos
# para despues traerlos en el campo de becas en la oferta academica


class Scholarship(models.Model):

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    who_can_apply = models.TextField(
        null=False,
        blank=False
    )

    application_process = models.TextField(
        null=False,
        blank=False
    )

    terms_and_conditions = models.TextField(
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = "Scholarship"
        verbose_name_plural = "Scholarships"

    def __str__(self):
        return self.name


class LodgingOfferType(models.Model):
    '''

    HOTEL = 'HOTEL'
    HOSTEL = 'HOSTEL'
    STUDENT_RESIDENCE = 'STUDENT_RESIDENCE'
    ACCOMODATION_WITH_LOCAL_FAMILY = 'ACCOMODATION_WITH_LOCAL_FAMILY'
    HOUSE_APT_SHARE_VISITANTS = 'HOUSE_APT_SHARE_VISITANTS'
    HOUSE_OR_PRIV_APT = 'HOUSE_OR_PRIV_APT'

    LODGING_OFFER_CHOICES = (
        (HOTEL, 'Hotel'),
        (HOSTEL, 'Hostel'),
        (STUDENT_RESIDENCE, 'Student Residence'),
        (ACCOMODATION_WITH_LOCAL_FAMILY, 'Accommodation with local family'),
        (HOUSE_APT_SHARE_VISITANTS, 'House or apartment to share with other visitors'),
        (HOUSE_OR_PRIV_APT, 'House or private apartment'),
    )
    '''

    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "Lodging Offer Type"
        verbose_name_plural = "Lodging Offer Type"

    def __str__(self):
        return self.name
