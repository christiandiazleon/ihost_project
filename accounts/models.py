from __future__ import unicode_literals
import json
from host_information.models import EntertainmentActivities, ResearchGroups, FeaturesAmenities, LodgingOfferType, SpeakLanguages

from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    # Model manager of all Django's user model

    PermissionsMixin
    # I have that the users that I create have groups permissions and
    # all benefits of them
)

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# from django.template.defaultfilters import slugify
from django.utils.text import slugify



# from languages_plus.models import Language
from django.conf import settings
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
# from countries_plus.models import Country
from phonenumber_field.modelfields import PhoneNumberField
# https://github.com/stefanfoulis/django-phonenumber-field

from smart_selects.db_fields import ChainedManyToManyField
from taggit.managers import TaggableManager


# Model Manager


class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        # If the users don't have a user or display name
        # I set as display_name the username they've provided.
        # If some reason signup some user without display_name, this will be
        # the username
        # if not display_name:
        #    display_name = username

        # Make new user, user instance in memory
        user  = self.model(
            # make sure that all the email addresses throughout your app are formatted the same way
            email = self.normalize_email(email),
            **extra_fields

        )
        user.set_password(password)
        # handle the encryption and validation checks and so.
        user.save()
        return user
    '''
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
            email = self.normalize_email(email)
            user = self.model(email = email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
    '''

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

    '''
    def create_superuser(self, email, username, display_name, password):
        user = self.create_user(
            email,
            username,
            display_name,
            password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    '''

class User(AbstractBaseUser, PermissionsMixin):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    SPANISH = 'SPA'
    ENGLISH = 'ENG'
    GERMAN = 'DEU'
    FRENCH = 'FRA'
    PORTUGUESE = 'POR'

    LANGUAGES_CHOICES = (
        (SPANISH, 'Spanish'),
        (ENGLISH, 'English'),
        (GERMAN, 'German'),
        (FRENCH, 'French'),
        (PORTUGUESE, 'Portuguese'),
    )

    ARTHISTIC_CULTURALS = 'ART_CULT'
    SPORTS = 'SPORTS'
    ECOLOGICAL = 'ECO'
    OUTDOOR_ACTIVITIES = 'OUTDOOR'
    SHOPPING = 'SHOPPING'
    TOURISM = 'TOURISM'
    NIGHT_LIFE = 'NIGHT_LIFE'
    THEMATIC_PARKS = 'FUN_PARKS'
    GASTRONOMY = 'GASTRONOMY'
    EVENTS_AND_SHOWS = 'EVENTS_SHOWS'
    MUSICALS = 'MUSICALS'
    LITERARY = 'LITERARY'

    PERSON = 'P'
    INSTITUTION = 'I'

    USER_TYPE_CHOICES = (
        (PERSON, "Person"),
        (INSTITUTION, "Institution"),
    )


    '''
    ENTERTAINMENT_ACTIVITIES_CHOICES = (
        (ARTHISTIC_CULTURALS, 'Arthistic-Culturals'),
        (ECOLOGICAL, 'Ecological'),
        (OUTDOOR_ACTIVITIES, 'Outdoor Activities'),
        (SHOPPING, 'Shopping'),
        (NIGHT_LIFE, 'Night Life'),
        (THEMATIC_PARKS, 'Thematics Parks'),
        (GASTRONOMY, 'Gastronomy'),
        (MUSICALS, 'Musicals'),
        (LITERARY, 'Literary'),
    )
    '''

    email = models.EmailField(unique=True, null=True,
            help_text=_('Required. Letters, digits and ''@/./+/-/_ only.'),
        validators=[RegexValidator(r'^[\w.@+-]+$', _('Enter a valid email address.'), 'invalid')
        ])


    username = models.CharField(_('username'), max_length=30, null=True,
            help_text=_('Required. 30 characters or fewer. Letters, digits and ''@/./+/-/_ only.'),
        validators=[RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
        ])

    slug = models.SlugField(
        # unique=True,
        max_length=100,
        blank=True
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)

    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    enterprise_name = models.CharField(_('enterprise name'), max_length=100, blank=True)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name='Gender',
        # default=False,
        blank=True,
    )

    country_of_origin = CountryField(blank_label='(select country)')

    city_of_origin = models.CharField(
        max_length=255,
        blank = False,
    )
    # Can I use later this package https://github.com/coderholic/django-cities

    country_current_residence = CountryField(
        blank_label='(select country)'
    )

    city_current_residence = models.CharField(
        max_length=255,
        blank = False,
    )
     # Can I use later this package https://github.com/coderholic/django-cities

    speak_languages = models.ManyToManyField(
        SpeakLanguages,
        help_text='What languages do you speak?',
        verbose_name='Languages',
        related_name="users",
        blank=True,
        # here m2m lookup sample
        # https://stackoverflow.com/a/16360605/2773461
    )

    phone_number = PhoneNumberField(
        blank=True,
        help_text="Please use the following format: <em>+Country Code-Number</em>.",
    )

    address = models.CharField(_("address"), max_length=128)

    bio = models.CharField(max_length=140, blank=True, default="")

    avatar = models.ImageField(
        upload_to='avatars',
        blank=True,
        null=True,
        verbose_name='Photo'
    )

    date_joined = models.DateTimeField(default=timezone.now)

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento',
        # help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        verbose_name='User type',
        default=False,
        blank=False,
    )

    is_student = models.BooleanField(
        default=False,
        verbose_name='Student',
        help_text='Student profile'
    )

    is_professor = models.BooleanField(
        default=False,
        verbose_name='Professor',
        help_text='Professor profile'
    )

    is_executive = models.BooleanField(
        default=False,
        verbose_name='Executive',
        help_text='Executive profile',
    )

    is_study_host = models.BooleanField(
        default=False,
        verbose_name='Study host',
        help_text='Study host profile',
    )

    is_innovation_host = models.BooleanField(
        default=False,
        verbose_name='Innovation host',
        help_text='Innovation host profile',
    )

    is_hosting_host = models.BooleanField(
        default=False,
        verbose_name='Hosting host',
        help_text='Hosting host profile',
    )

    is_entertainment_host = models.BooleanField(
        default=False,
        verbose_name='Entertainment host',
        help_text='Entertainment host profile',
    )

    is_other_services_host = models.BooleanField(
        default=False,
        verbose_name='Other services host',
        help_text='Other services host profile',
    )

    entertainment_activities = models.ManyToManyField(
        EntertainmentActivities,
        blank=True,
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    # email is the unique identifier to look people up in the database
    # currently we have the username too, but I want to log in with the
    # email addresses
    USERNAME_FIELD = "email"

    # List of fields that will be sent when create the superuser in addition to
    # username and password
    # REQUIRED_FIELDS = ["display_name", "username"]
    # REQUIRED_FIELDS = ["display_name",]

    class Meta:
        db_table = 'auth_user'
        verbose_name_plural = 'Usuarios en la plataforma'

    def __str__(self):
        return "@{}".format(self.email)

    '''
    def setspeak_languages(self, days):
        self.days = json.dumps(self.speak_languages)

    def getspeak_languages(self):
        return json.loads(self.speak_languages)
    '''

    @property
    def image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

    def get_short_name(self):
        return self.first_name
        #return self.display_name

    def get_long_name(self):
        return "{} (@{})".format(self.first_name, self.last_name)
        # return "{} (@{})".format(self.display_name, self.username)

    # We get the profiles user according with their type

    def get_student_profile(self):
        student_profile = None
        if hasattr(self, 'studentprofile'):
            student_profile = self.studentprofile
        return student_profile

    def get_professor_profile(self):
        professor_profile = None
        if hasattr(self, 'professorprofile'):
            professor_profile = self.professorprofile
        return professor_profile

    def get_executive_profile(self):
        executive_profile = None
        if hasattr(self, 'executiveprofile'):
            executive_profile = self.executiveprofile
        return executive_profile

    def get_study_host_profile(self):
        study_host_profile = None
        if hasattr(self, 'studyhostprofile'):
            study_host_profile = self.studyhostprofile
        return study_host_profile

    def get_innovation_host_profile(self):
        innovation_host_profile = None
        if hasattr(self, 'innovationhostprofile'):
            innovation_host_profile = self.innovationhostprofile
        return innovation_host_profile

    def get_hosting_host_profile(self):
        hosting_host_profile = None
        if hasattr(self, 'hostinghostprofile'):
            hosting_host_profile = self.hostinghostprofile
        return hosting_host_profile

    def get_entertainment_host_profile(self):
        entertainment_host_profile = None
        if hasattr(self, 'entertainmenthostprofile'):
            entertainment_host_profile = self.entertainmenthostprofile
        return entertainment_host_profile

    def get_other_services_host_profile(self):
        other_services_host_profile = None
        if hasattr(self, 'otherserviceshostprofile'):
            other_services_host_profile = self.otherserviceshostprofile
        return other_services_host_profile

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        if self.is_student and getattr(self, 'studentprofile', None) is None:
            StudentProfile.objects.create(
                user=self,
                slug = self.email
            )
        if self.is_professor and getattr(self, 'professorprofile', None) is None:
            ProfessorProfile.objects.create(
                user=self,
                slug=self.email
            )
        if self.is_executive and getattr(self, 'executiveprofile', None) is None:
            ExecutiveProfile.objects.create(
                user=self,
                slug=self.email
            )
        if self.is_study_host and getattr(self, 'studyhostprofile', None) is None:
            StudyHostProfile.objects.create(
                user=self,
                slug=self.email
            )
        if self.is_hosting_host and getattr(self, 'hostinghostprofile', None) is None:
            HostingHostProfile.objects.create(
                user=self,
                slug=self.email
            )

# https://docs.djangoproject.com/en/1.11/ref/signals/#django.db.models.signals.pre_save


def create_slug(instance, new_slug=None):
    slug = slugify(instance.email)
    if new_slug is not None:
        slug = new_slug
    qs = User.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        # Add the id to slug (compose by email + ID)
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_user_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    """
    slug = slugify(instance.email)
    # fabiola.quimica - fabiolaquimica
    # We want to make sure that slug doesn't already exist
    # I will check if exist with a filter
    exists = User.objects.filter(slug=slug).exists()
    if exists:
        # Add the id to slug (compose by email + ID)
        slug = "%s-%s" %(slugify(instance.email), instance.id)

    instance.slug = slug
    """

pre_save.connect(pre_save_user_receiver, sender=settings.AUTH_USER_MODEL)

'''
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(sender, instance, **kwargs):
    slug = slugify(instance.email)
    User.objects.filter(pk=instance.pk).update(slug=slug)
'''

class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()

        return qs

# volvera ver Model Manager for following https://www.udemy.com/tweetme-django/learn/v4/t/lecture/6134698?start=0 y el de signals

class UserProfile(models.Model):
    # user.profile
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    # user.profile.following -- users I follow
    # user.profile.followed_by -- users that follow me -- reverse relationship
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='followed_by'
    )

    objects = UserProfileManager() # UserProfile.objects.all()
    # abc = UserProfileManager() # UserProfile.abc.all()

    def __str__(self):
        # return str(self.following.all.count())
        return str(self.user)

    def get_following(self):
        users = self.following.all() # Users.objects.all().exclude(email=self.user.email)
        return users.exclude(email=self.user.email)

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
# get_or_create (user_obj true/false)
def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    print(instance)
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)
        # celery + redis
        # deferred tasks

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)


class StudentProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    origin_education_school = models.CharField(
        _("Origin education institute"), max_length=128
    )

    current_education_school = models.CharField(
        _("Institution of education to which is linked in the current residence"), max_length=128
    )

    extra_occupation = models.CharField(
        _("Extra occupation"), max_length=128
    )

    educational_titles = models.CharField(
        max_length=255,
    )

    complete_studies_school = models.CharField(
        _("Institution where completed his previous studies"), max_length=255
    )

    knowledge_topics_choice = models.CharField(
        _("Areas of knowledge of your choice"), max_length=255
    )


    class Meta:
        verbose_name_plural='Usuarios con perfil de estudiantes'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class ProfessorProfile(models.Model):

    CATHEDRAL_PROFESSOR = 'CATHEDRAL'
    RESEARCH_PROFESSOR = 'RESEARCH'
    INSTITUTIONAL_DIRECTIVE = 'DIRECTIVE'

    OCCUPATION_CHOICES = (
        (CATHEDRAL_PROFESSOR, 'Cathedral Professor'),
        (RESEARCH_PROFESSOR, 'Research Professor'),
        (INSTITUTIONAL_DIRECTIVE, 'Institutional Directive'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    occupation = models.CharField(
        max_length=255,
        blank = False,
    )

    origin_education_school = models.CharField(
        _("Origin education institute"), max_length=128
    )

    current_education_school = models.CharField(
        _("Institution of education to which is linked in the current residence"), max_length=128
    )

    educational_titles = models.CharField(
        max_length=255,
    )

    complete_studies_school = models.CharField(
        _("Institution where completed his previous studies"), max_length=255
    )

    knowledge_topics_choice = models.CharField(
        _("Areas of knowledge of your choice"), max_length=255
    )

    research_groups = models.CharField(
        _("Research groups to which it belongs"), max_length=255
    )

    autorship_publications = models.CharField(
        _("Publications of its authorship"), max_length=255
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de profesores'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class ExecutiveProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    occupation = models.CharField(
        max_length=255,
        blank = True,
        verbose_name='Occupation',
    )

    enterprise_name = models.CharField(
        max_length=255,
        blank = False,
        verbose_name='Company to which you are linked',
    )

    companies_to_visit = models.CharField(
        _("Companies to Visit"), max_length=255
    )

    educational_titles = models.CharField(
        max_length=255,
    )

    complete_studies_school = models.CharField(
        _("Institution where completed his previous studies"), max_length=255
    )

    innovation_topics_choice = models.CharField(
        _("Areas of innovation of your choice"), max_length=255
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de ejecutivos'

    def __str__(self):
        return "{}".format(self.user.display_name,)




class StudyHostProfile(models.Model):

    UNIVERSITY = 'UNIVERSITY'
    TECHNOLOGICAL_SCHOOL = 'TECH_SCHOOL'
    UNIVERSITY_INSTITUTION = 'UNIV_INST'
    PROFESSIONAL_TECH_INSTITUTION = 'PROF_TECH_INST'
    CEC = 'CONTINUAL_EDUCATION_CENTER'

    INSTITUTION_TYPE_CHOICES = (
        (UNIVERSITY, 'University'),
        (TECHNOLOGICAL_SCHOOL, 'Technological School'),
        (UNIVERSITY_INSTITUTION, 'University Institution'),
        (PROFESSIONAL_TECH_INSTITUTION, 'Professional Technological Institution'),
        (CEC, 'Continual Education Center'),
    )

    PRIVATE = 'PRIVATE'
    PUBLIC = 'PUBLIC'
    MIXED = 'MIXED'

    CHARACTER_INSTITUTE_CHOICES = (
        (PRIVATE, "Private"),
        (PUBLIC, "Public"),
        (MIXED, "Private - Public"),
    )

    NATIONAL_ACCREDITATIONS = 'NAT_ACC'
    INTERNATIONAL_ACCREDITATIONS = 'INT_ACC'

    ACCREDITATIONS_CHOICES = (
        (NATIONAL_ACCREDITATIONS, "National Accreditation"),
        (INTERNATIONAL_ACCREDITATIONS, "International Accreditation"),
    )

    LESS_THAN_THOUSAND = 'Less than a thousand students'
    ONE_THOUSAND_TEN_THOUSAND = 'Between one thousand and ten thousand students'
    TEN_THOUSAND_TWENTY_THOUSAND = 'Between ten thousand and twenty thousand students'
    GREATER_THAN_TWENTY_THOUSAND = 'More/Greater than twenty thousand students'


    STUDENT_NUMBERS_CHOICES = (
        (LESS_THAN_THOUSAND, 'Less than a thousand students'),
        (ONE_THOUSAND_TEN_THOUSAND, 'Between one thousand and ten thousand students'),
        (TEN_THOUSAND_TWENTY_THOUSAND, 'Between ten thousand and twenty thousand students'),
        (GREATER_THAN_TWENTY_THOUSAND, 'More/Greater than twenty thousand students'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    institution_type = models.CharField(
        max_length=255,
        choices=INSTITUTION_TYPE_CHOICES,
        verbose_name='Institution Type',
    )

    institute_character = models.CharField(
        max_length=7,
        choices=CHARACTER_INSTITUTE_CHOICES,
        verbose_name='Character of the institution',
    )

    high_quality_accreditations = models.CharField(
        _("Accreditations of high quality"), max_length=255
    )

    students_number = models.CharField(
        max_length=255,
        choices=STUDENT_NUMBERS_CHOICES,
        verbose_name='Number of students'
    )

    rankings_classification = models.CharField(
        _("Classification in ranking"), max_length=255
    )

    knowledge_topics = TaggableManager(
        verbose_name="Knowledge topics",
        # help_text= tag_helptext()
        help_text=_("A comma-separated list of topics.")
    )

    strengths = models.CharField(
        _("Strengths"), max_length=255
    )


    # TO-DO Consultar las grupos del usuario studyhost solamente

    research_groups = models.ManyToManyField(
        ResearchGroups,
        help_text='What are your research groups?',
        verbose_name='Research Groups'
    )

    photography = models.ImageField(
        upload_to='studyhosts',
        blank=True,
        null=True,
        verbose_name='Photo'
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de estudio'

    def __str__(self):
        return "{}".format(self.user.display_name,)

    '''
    def tag_helptext():
        help_text = "Options: "
        for t in Tag.objects.all():
            help_text += t.name + " ||| "
        return help_text
    '''


class InnovationHostProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de innovación'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class HostingHostProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    lodging_offer_type = models.ManyToManyField(
        LodgingOfferType,
        help_text='What lodging offer type?',
        verbose_name='Lodging Offer Type'
    )

    featured_amenities = models.ManyToManyField(
        FeaturesAmenities,
        help_text='What amenities do you offer?',
        verbose_name='Featured Amenities'
    )


    stars = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Stars',
        help_text='Number of stars'
    )

    photography = models.ImageField(
        upload_to='hostinghosts',
        blank=True,
        null=True,
        verbose_name='Photo'
    )

    additional_description = models.TextField(
        null=False,
        blank=False
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de hospedaje'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class EntertainmentHostProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de entretenimiento'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class OtherServicesHostProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de servicios varios'

    def __str__(self):
        return "{}".format(self.user.display_name,)
