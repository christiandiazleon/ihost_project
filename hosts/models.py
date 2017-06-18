from __future__ import unicode_literals
from django.db import models
from host_information.models import (LodgingServiceOffer, FeaturesAmenities, RoomInformation, Scholarship)

from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from smart_selects.db_fields import ChainedManyToManyField

from django.contrib.auth import get_user_model
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class LodgingOffer(models.Model):

    ALL_PROPERTY = 'All property'
    PRIVATE_ROOM = 'Private Room'
    SHARED_ROOM = 'Shared Room'

    ROOM_TYPE_OFFERED_CHOICES = (
        (ALL_PROPERTY, "All property"),
        (PRIVATE_ROOM, "Private Room"),
        (SHARED_ROOM, "Shared Room"),
    )

    ONE_GUEST = 'For 1 guest'
    TWO_GUESTS = 'For 2 guests'
    THREE_GUESTS = '3 guests'
    FOUR_GUESTS = '4 guests'
    FIVE_GUESTS = '5 guests'
    SIX_GUESTS = '6 guests'
    SEVEN_GUESTS = '7 guests'
    EIGHT_GUESTS = '8 guests'
    NINE_GUESTS = '9 guests'
    TEN_GUESTS = '10 guests'


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

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    # Fijarle un max_length
    ad_title = models.CharField(
        null=False,
        blank=False,
        max_length=255
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
        verbose_name='Offered Services',
        related_name="lodgingoffers"
        # here m2m lookup sample
        # https://stackoverflow.com/a/16360605/2773461
    )

    room_type_offered = models.CharField(
        max_length=255,
        choices=ROOM_TYPE_OFFERED_CHOICES,
        verbose_name='Room Type Offered',
    )

    number_guest_room_type = models.CharField(
        max_length=255,
        choices=NUMBER_GUESS_ROOM_TYPE_CHOICES,
        verbose_name='Number guess in room',
    )

    room_information = models.ManyToManyField(
        RoomInformation,
        help_text='Room caracteristics',
        verbose_name='Room caracteristics',
        related_name="lodgingoffers"
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

    def __str__(self):
        return "%s" % self.ad_title

    def get_absolute_url(self):
        return u'/host/lodging-offer/%d' % self.id


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

    ACADEMIC_SEMESTER = 'Academic Semester'
    RESEARCH = 'Research'
    ROTATIONS_OR_PRACTICES = 'Rotations or Practices'
    SUMMER_SCHOOL = 'Summer School'

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

    '''
    slug = models.SlugField(
        max_length=100,
        blank=True
    )
    '''

    knowledge_topics = TaggableManager(
        verbose_name="Knowledge topics",
        help_text=_("A comma-separated list of topics.")
    )

    studies_type_offered = models.ManyToManyField(
        StudiesTypeOffered,
        verbose_name=u'Studies Type offered',
        related_name="studiesofferts"
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

    additional_description = models.TextField(
        null=False,
        blank=False
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

    def get_absolute_url(self):
        return "/host/study-offer/%i/" % self.id
    '''
    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
    '''

