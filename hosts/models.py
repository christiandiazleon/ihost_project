from __future__ import unicode_literals
from django.db import models
from host_information.models import (LodgingServiceOffer, FeaturesAmenities, RoomInformation, Scholarship)

from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from smart_selects.db_fields import ChainedManyToManyField

from django.contrib.auth import get_user_model
from django.conf import settings


class LodgingOffer(models.Model):

    ALL_PROPERTY = 'ALL_PROPERTY'
    PRIVATE_ROOM = 'PRIVATE_ROOM'
    SHARED_ROOM = 'SHARED_ROOM'

    ROOM_TYPE_OFFERED_CHOICES = (
        (ALL_PROPERTY, "All property"),
        (PRIVATE_ROOM, "Private Room"),
        (SHARED_ROOM, "Shared Room"),
    )

    ONE_GUEST = 'ONE_GUEST'
    TWO_GUESTS = 'ONE_GUEST'
    THREE_GUESTS = 'ONE_GUEST'
    FOUR_GUESTS = 'ONE_GUEST'
    FIVE_GUESTS = 'ONE_GUEST'
    SIX_GUESTS = 'ONE_GUEST'
    SEVEN_GUESTS = 'ONE_GUEST'
    EIGHT_GUESTS = 'ONE_GUEST'
    NINE_GUESTS = 'ONE_GUEST'
    TEN_GUESTS = 'ONE_GUEST'


    NUMBER_GUESS_ROOM_TYPE_CHOICES = (
        (ONE_GUEST, "For 1 guest"),
        (TWO_GUESTS, "For 2 guests"),
        (THREE_GUESTS, "For 3 guests"),
        (FOUR_GUESTS, "For 4 guests"),
        (FIVE_GUESTS, "For 5 guests"),
        (SIX_GUESTS, "For 6 guests"),
        (SEVEN_GUESTS, "For 7 guests"),
        (EIGHT_GUESTS, "For 8 guests"),
        (NINE_GUESTS, "For 9 guests"),
        (TEN_GUESTS, "For 10 guests"),
    )

    '''
    hosting_host_user = models.ForeignKey(
        'accounts.HostingHostProfile',
        null=True,
        blank=True,
        verbose_name='Hosting Host',
        related_name='hostinghostprofile'
    )
    '''
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    ad_title = models.TextField(
        null=False,
        blank=False
    )

    available_dates = models.DateField(
        blank=True,
        null=True,
        verbose_name='Available dates',
        help_text="Days in which is possible bookings",
    )

    '''
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

    birth_year = models.DateField(
        blank=True,
        null=True,
        verbose_name='Available dates',
        help_text="Days in which is possible bookings",
    )




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

    room_type_offered = models.CharField(
        max_length=255,
        choices=ROOM_TYPE_OFFERED_CHOICES,
        verbose_name='Room Type Offered',
    )

    number_guest_room_type = models.CharField(
        max_length=255,
        choices=NUMBER_GUESS_ROOM_TYPE_CHOICES,
        verbose_name='Room Type Offered',
    )

    room_information = models.ManyToManyField(
        RoomInformation,
        help_text='Room caracteristics',
        verbose_name='Room caracteristics'
    )

    photographies = models.ImageField(
        upload_to='hosting-host-photos',
        blank=True,
        null=True,
        verbose_name='Photographies'
    )

    room_value = models.CharField(_("Price"), max_length=128)

    additional_description = models.TextField(
        null=False,
        blank=False
    )

    '''
    def get_absolute_url(self):
        return u'/become-a-host/lodging-host/offer/new/%d' % self.id
    '''

# Relacionarlo con el studyhost y que este pueda ingresarlos
# para despues traerlos en el campo de studies_type_offered  en el perfil


class StudiesTypeOffered(models.Model):

    CONTINUING_EDUCATION_STUDIES = 'Continuing Education studies'
    TECHNIQUE = 'Technique'
    TECHNOLOGY = 'Technology'
    PROFESSIONAL = 'Professional'
    SPECIALIZATION = 'Specialization'
    MASTER = 'Master'
    DOCTORATE = 'Doctorate'

    STUDIES_TYPE_CHOICES = (
        (CONTINUING_EDUCATION_STUDIES, u'Continuing Education studies'),
        (TECHNIQUE, u'Technique'),
        (TECHNOLOGY, u'Technology'),
        (PROFESSIONAL, u'Professional'),
        (SPECIALIZATION, u'Specialization'),
        (MASTER, u'Master'),
        (DOCTORATE, u'Doctorate'),
    )

    name = models.CharField(
        max_length=100,
        choices=STUDIES_TYPE_CHOICES,
        blank=False,
        verbose_name=u'nombre',
    )

    class Meta:
        verbose_name = "Tipo de estudio ofertado"
        verbose_name_plural = "Tipo de estudios ofertados"

    def __str__(self):
        return "%s" % self.name

# Relacionarlo con el studyhost y que este pueda ingresarlos
# para despues traerlos en el campo de studies_offert_list  en el perfil


class StudiesOffertList(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name = u'nombre'
    )

    studies_type_offered_associated = models.ManyToManyField(
        StudiesTypeOffered,
        blank=True,
        verbose_name='Tipo de oferta asociada'
    )

    class Meta:
        verbose_name = "Oferta de estudios"
        verbose_name_plural = "Oferta de estudios"

    def __str__(self):
        return "%s" % self.name


class StudiesOffert(models.Model):

    ACADEMIC_SEMESTER = 'ACADEMIC_SEMESTER'
    RESEARCH = 'RESEARCH'
    ROTATIONS_OR_PRACTICES = 'ROTATIONS_OR_PRACTICES'
    SUMMER_SCHOOL = 'SUMMER_SCHOOL'

    ACADEMIC_MOBILITY_PROGRAMS_CHOICES = (
        (ACADEMIC_SEMESTER, 'Academic Semester'),
        (RESEARCH, 'Research'),
        (ROTATIONS_OR_PRACTICES, 'Rotations or practices'),
        (SUMMER_SCHOOL, 'Summer School'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    ad_title = models.TextField(
        null=False,
        blank=False
    )

    knowledge_topics = TaggableManager(
        verbose_name="Knowledge topics",
        help_text=_("A comma-separated list of topics.")
    )

    studies_type_offered = models.ManyToManyField(
        'StudiesTypeOffered',
        verbose_name=u'Studies Type offered'
    )

    studies_offert_list = ChainedManyToManyField(
        'StudiesOffertList', # Modelo encadenado
        horizontal=False,
        verbose_name='Studies Offert List',
        chained_field='studies_type_offered',
        chained_model_field='studies_type_offered_associated',
        help_text='What are your studies offerts?',
        blank=True,
    )

    academic_mobility_programs = models.CharField(
        max_length=255,
        choices=ACADEMIC_MOBILITY_PROGRAMS_CHOICES,
        verbose_name='Academic mobility programs',
        help_text='Available student academic mobility programs',
    )


    # TO-DO Consultar las becas del usuario studyhost solamente
    scholarships = models.ManyToManyField(
        Scholarship,
        help_text='Scholarships availables',
        verbose_name='Scholarships',
        blank=True,
    )

    photo = models.ImageField(
        upload_to='study-host-offert-photos',
        blank=True,
        verbose_name='Photography',
        null=True
    )

    def __str__(self):
        return "{}".format(self.ad_title)
