from __future__ import unicode_literals

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    # Model manager of all Django's user model

    PermissionsMixin
    # I have that the users that I create have groups permissions and
    # all benefits of them
)

from django.conf import settings
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


# Model Manager
class UserManager(BaseUserManager):

    def create_user(self, email, username, display_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        # If the users don't have a user or display name
        # I set as display_name the username they've provided.
        # If some reason signup some user without display_name, this will be the username
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

    email = models.EmailField(unique=True)

    username = models.CharField(max_length=40, unique=True)

    display_name = models.CharField(max_length=140)

    gender = models.CharField(
        max_length=4,
        choices=GENDER_CHOICES,
        verbose_name='genero'

    )

    country_of_origin = CountryField(blank_label='(select country)')

    bio = models.CharField(max_length=140, blank=True, default="")

    avatar = models.ImageField(blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento',
        help_text="Por favor use el siguiente formato: <em>DD/MM/YYYY</em>.",
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
        return self.display_name

    def get_long_name(self):
        return "{} (@{})".format(self.display_name, self.username)


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural='Usuarios con perfil de estudiantes'

    def __str__(self):
        return "{}".format(self.user.display_name,)


class ProfessorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
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
