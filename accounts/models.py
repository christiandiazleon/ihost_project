from __future__ import unicode_literals
import json
from host_information.models import EntertainmentActivities

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

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


# from languages_plus.models import Language
from django.conf import settings
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
# from countries_plus.models import Country
from phonenumber_field.modelfields import PhoneNumberField
# https://github.com/stefanfoulis/django-phonenumber-field

# Model Manager


class UserManager(BaseUserManager):

    def create_user(self, email, username, display_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        # If the users don't have a user or display name
        # I set as display_name the username they've provided.
        # If some reason signup some user without display_name, this will be
        # the username
        if not display_name:
            display_name = username

        # Make new user, user instance in memory
        user  = self.model(
            # make sure that all the email addresses throughout your app are formatted the same way
            email = self.normalize_email(email),
            username = username,
            display_name = display_name
        )
        user.set_password(password)
        # handle the encryption and validation checks and so.
        user.save()
        return user

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


class User(AbstractBaseUser, PermissionsMixin):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, "Masculino"),
        (FEMALE, "Femenino"),
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

    email = models.EmailField(unique=True,
            help_text=_('Required. Letters, digits and ''@/./+/-/_ only.'),
        validators=[RegexValidator(r'^[\w.@+-]+$', _('Enter a valid email address.'), 'invalid')
        ])

    # username = models.CharField(max_length=40, unique=True)

    username = models.CharField(_('username'), max_length=30, unique=True,
            help_text=_('Required. 30 characters or fewer. Letters, digits and ''@/./+/-/_ only.'),
        validators=[RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
        ])

    slug = models.SlugField(
        max_length=100,
        blank=True
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)

    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    display_name = models.CharField(max_length=140)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name='genero',
        default=False,
        blank=False,
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

    # speak_languages = Country.objects.get(iso3='USA')
    speak_languages = models.CharField(
        max_length=255,
        # choices=LANGUAGES_CHOICES,
        # verbose_name='Speak languages',
        blank = False,

    )

    phone_number = PhoneNumberField(
        blank=True,
        help_text="Please use the following format: <em>+Country Code-Number</em>.",
    )

    address = models.CharField(_("address"), max_length=128)

    bio = models.CharField(max_length=140, blank=True, default="")

    avatar = models.ImageField(blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento',
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
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

    '''
    entertainment_activities_choice = models.CharField(
        _("Entertainment activities of your choice"), max_length=255
    )
    '''
    entertainment_activities = models.ManyToManyField(EntertainmentActivities)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # email is the unique identifier to look people up in the database
    # currently we have the username too, but I want to log in with the
    # email addresses
    USERNAME_FIELD = "email"

    # List of fields that will be sent when create the superuser in addition to
    # username and password
    REQUIRED_FIELDS = ["display_name", "username"]

    class Meta:
        db_table = 'auth_user'
        verbose_name_plural = 'Usuarios en la plataforma'

    def __str__(self):
        return "@{}".format(self.username)

    def setspeak_languages(self, days):
        self.days = json.dumps(self.speak_languages)

    def getspeak_languages(self):
        return json.loads(self.speak_languages)

    def get_short_name(self):
        return self.first_name
        #return self.display_name

    def get_long_name(self):
        return "{} (@{})".format(self.display_name, self.username)

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
                slug = self.username
            )
        if self.is_professor and getattr(self, 'professorprofile', None) is None:
            ProfessorProfile.objects.create(
                user=self,
                slug=self.username
            )
        if self.is_executive and getattr(self, 'executiveprofile', None) is None:
            ExecutiveProfile.objects.create(
                user=self,
                slug=self.username
            )
        if self.is_study_host and getattr(self, 'studyhostprofile', None) is None:
            StudyHostProfile.objects.create(
                user=self,
                slug=self.username
            )
        if self.is_hosting_host and getattr(self, 'hostinghostprofile', None) is None:
            HostingHostProfile.objects.create(
                user=self,
                slug=self.username
            )
        '''
        user = super(User,self).save(*args,**kwargs)

        # Creating an user with student, professor and executive profiles
        if self.is_student and not StudentProfile.objects.filter(user=self).exists() \
            and self.is_professor and not ProfessorProfile.objects.filter(user=self).exists() \
            and self.is_executive and not ExecutiveProfile.objects.filter(user=self).exists():
            student_profile = StudentProfile(user=self)
            student_slug = self.username
            student_profile.slug = student_slug

            professor_profile = ProfessorProfile(user=self)
            professor_slug = self.username
            professor_profile.slug = professor_slug

            executive_profile = ExecutiveProfile(user=self)
            executive_slug = self.username
            executive_profile.slug = executive_slug

            student_profile.save()
            professor_profile.save()
            executive_profile.save()

        # Creating an user with student profile
        elif self.is_student and not StudentProfile.objects.filter(user=self).exists():
            student_profile = StudentProfile(user = self)
            student_slug = self.username
            student_profile.slug = student_slug

            student_profile.save()

        # Creating an user with professor profile
        elif self.is_professor and not ProfessorProfile.objects.filter(user=self).exists():
            professor_profile = ProfessorProfile(user=self)
            professor_slug = self.username
            professor_profile.slug = professor_slug
            professor_profile.save()

        # Creating an user with executive profile
        elif self.is_executive and not ExecutiveProfile.objects.filter(user=self).exists():
            executive_profile = ExecutiveProfile(user = self)
            executive_slug = self.username
            executive_profile.slug = executive_slug
            executive_profile.save()

        # Creating an user with study host profile
        elif self.is_study_host and not StudyHostProfile.objects.filter(user=self).exists():
            study_host_profile = StudyHostProfile(user = self)
            study_host_slug = self.username
            study_host_profile.slug = study_host_slug
            study_host_profile.save()

        # Creating an user with innovation host profile
        elif self.is_innovation_host and not InnovationHostProfile.objects.filter(user=self).exists():
            innovation_host_profile = InnovationHostProfile(user = self)
            innovation_host_slug = self.username
            innovation_host_profile.slug = innovation_host_slug
            innovation_host_profile.save()

        # Creating an user with entertainment host profile
        elif self.is_entertainment_host and not EntertainmentHostProfile.objects.filter(user=self).exists():
            entertainment_host_profile = EntertainmentHostProfile(user = self)
            entertainment_host_slug = self.username
            entertainment_host_profile.slug = entertainment_host_slug
            entertainment_host_profile.save()

        # Creating an user with other services host profile
        elif self.is_other_services_host and not OtherServicesHostProfile.objects.filter(user=self).exists():
            entertainment_host_profile = EntertainmentHostProfile(user = self)
            entertainment_host_slug = self.username
            entertainment_host_profile.slug = entertainment_host_slug
            entertainment_host_profile.save()
        '''

@receiver(post_save, sender=User)
def post_save_user(sender, instance, **kwargs):
    slug = slugify(instance.username)
    User.objects.filter(pk=instance.pk).update(slug=slug)


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

    CES = 'CONT_EDUCATION_'
    TECHNIQUE_STUDIES = 'TECHNIQUE'
    TECHNOLOGICAL_STUDIES = 'TECHNOLOGICAL'
    PROFESSIONAL_STUDIES = 'PROFESSIONAL'
    SPECIALIZATION_STUDIES = 'SPECIALIZATION'
    MASTER_STUDIES = 'MASTER'
    DOCTORATE = 'DOCTORATE'

    STUDIES_TYPE_OFFERED_CHOICES = (
        (CES, 'Continuing education studies'),
        (TECHNIQUE_STUDIES, 'Technique'),
        (TECHNOLOGICAL_STUDIES, 'Technology'),
        (PROFESSIONAL_TECH_INSTITUTION, 'Professional'),
        (SPECIALIZATION_STUDIES, 'Specialization'),
        (MASTER_STUDIES, 'Master'),
        (DOCTORATE, 'Doctorate'),
    )

    STUDIES_OFFERT_LIST_CHOICES = (
        ('Continuing education studies', (
            ('SPANISH_FOREIGNS', 'Spanish for foreigns'),
            ('ENGLISH', 'English'),
            )
        ),
        ('Professional', (
            ('SYSTEMS_ENGINEERING', 'Systems Engineering'),
            ('BIOMEDICAL_ENGINEERING', 'Biomedical Engineering'),
            )
        ),
        ('unknown', 'Unknown'),
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
        _("Institution type"), max_length=255
    )

    institute_character = models.CharField(
        max_length=7,
        choices=CHARACTER_INSTITUTE_CHOICES,
        verbose_name='Character of the institution',
        default=False,
        blank=False,
    )

    high_quality_accreditations = models.CharField(
        _("Accreditations of high quality"), max_length=255
    )

    students_number = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Number of students',
    )

    rankings_classification = models.CharField(
        _("Classification in ranking"), max_length=255
    )

    knowledge_topics_choice = models.CharField(
        _("Areas of knowledge of your choice"), max_length=255
    )

    strengths = models.CharField(
        _("Strengths"), max_length=255
    )

    studies_type_offered = models.CharField(
        _("Type of studies offered"), max_length=255
    )

    studies_offert_list = models.CharField(
        _("Studies Offert List"), max_length=255,
        choices = STUDIES_OFFERT_LIST_CHOICES
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de estudio'

    def __str__(self):
        return "{}".format(self.user.display_name,)


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
