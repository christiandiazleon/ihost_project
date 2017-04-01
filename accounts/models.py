from __future__ import unicode_literals
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

    email = models.EmailField(unique=True)

    #username = models.CharField(max_length=40, unique=True)

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

    # speak_languages = Country.objects.get(iso3='USA')
    speak_languages = models.CharField(
        max_length=255,
        # choices=LANGUAGES_CHOICES,
        # verbose_name='Speak languages',
        blank = False,

    )

    phone_number = PhoneNumberField(blank=True)

    address = models.CharField(_("address"), max_length=128)

    bio = models.CharField(max_length=140, blank=True, default="")

    avatar = models.ImageField(blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento',
        help_text="Por favor use el siguiente formato: <em>DD/MM/YYYY</em>.",
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

    def save(self, *args, **kwargs):
        user = super(User,self).save(*args,**kwargs)

        # Creating an user with student, professor and executive profiles
        if self.is_student and not StudentProfile.objects.filter(user=self).exists() \
            and self.is_professor and not ProfessorProfile.objects.filter(user=self).exists() \
            and self.is_executive and not ExecutiveProfile.objects.filter(user=self).exists():
            student_profile = StudentProfile(user=self)
            student_slug = self.username
            student_profile.slug = student_slug

            professor_profile = ProfessorProfile(user=self)
            executive_profile = ExecutiveProfile(user=self)

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
            professor_profile.save()

        # Creating an user with executive profile
        elif self.is_executive and not ExecutiveProfile.objects.filter(user=self).exists():
            executive_profile = ExecutiveProfile(user = self)
            executive_profile.save()


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
        _("origin education institute"), max_length=128
    )

    current_education_school = models.CharField(
        _("current education institute"), max_length=128
    )

    extra_occupation = models.CharField(
        _("extra occupation"), max_length=128
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

    # educational_titles =

    class Meta:
        verbose_name_plural='Usuarios con perfil de profesores'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class ExecutiveProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de ejecutivos'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class StudyHostProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
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

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de innovación'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class HostingHostProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
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

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de entretenimiento'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class OtherServicesHostProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de anfitriones de servicios varios'

    def __str__(self):
        return "{}".format(self.user.display_name,)
