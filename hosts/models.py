from __future__ import unicode_literals
from django.db import models
from host_information.models import (
    LodgingServiceOffer, FeaturesAmenities, RoomInformation)

from django.utils.translation import ugettext_lazy as _


class LodgingOffer(models.Model):

    hosting_host_user = models.ForeignKey(
        'accounts.HostingHostProfile',
        null=True,
        blank=True,
        verbose_name='Hosting Host',
        related_name='hostinghostprofile'
    )

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

    lodging_offer_type = models.CharField(
        max_length=100,
        choices=LODGING_OFFER_CHOICES
    )

    '''
    check_in = models.DateField(
        blank=True,
        null=True,
        verbose_name='Check In',
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
    )

    check_out = models.DateField(
        blank=True,
        null=True,
        verbose_name='Check Out',
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
    )
    '''
    offered_services = models.ManyToManyField(
        LodgingServiceOffer,
        help_text='What services do you offer?',
        verbose_name='Offered Services'
    )

    featured_amenities = models.ManyToManyField(
        FeaturesAmenities,
        help_text='What amenities do you offer?',
        verbose_name='Featured Amenities'
    )

    room_information = models.ManyToManyField(
        RoomInformation,
        help_text='Room caracteristics',
        verbose_name='Room caracteristics'
    )

    scene = models.ImageField(blank=True, null=True)

    room_value = models.CharField(_("Price"), max_length=128)

    additional_description = models.CharField(max_length=140, blank=True, default="")

    def get_absolute_url(self):
        return u'/become-a-host/lodging-host/offer/new/%d' % self.id


