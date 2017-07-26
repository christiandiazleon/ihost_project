# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 05:16
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('host_information', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='Required. Letters, digits and @/./+/-/_ only.', max_length=254, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid email address.', 'invalid')])),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('enterprise_name', models.CharField(blank=True, max_length=100, verbose_name='enterprise name')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10, verbose_name='Gender')),
                ('country_of_origin', django_countries.fields.CountryField(max_length=2)),
                ('city_of_origin', models.CharField(max_length=255)),
                ('country_current_residence', django_countries.fields.CountryField(max_length=2)),
                ('city_current_residence', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Please use the following format: <em>+Country Code-Number</em>.', max_length=128)),
                ('address', models.CharField(max_length=128, verbose_name='address')),
                ('bio', models.CharField(blank=True, default='', max_length=140)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Photo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('user_type', models.CharField(choices=[('P', 'Person'), ('I', 'Institution')], default=False, max_length=10, verbose_name='User type')),
                ('is_student', models.BooleanField(default=False, help_text='Student profile', verbose_name='Student')),
                ('is_professor', models.BooleanField(default=False, help_text='Professor profile', verbose_name='Professor')),
                ('is_executive', models.BooleanField(default=False, help_text='Executive profile', verbose_name='Executive')),
                ('is_study_host', models.BooleanField(default=False, help_text='Study host profile', verbose_name='Study host')),
                ('is_innovation_host', models.BooleanField(default=False, help_text='Innovation host profile', verbose_name='Innovation host')),
                ('is_hosting_host', models.BooleanField(default=False, help_text='Hosting host profile', verbose_name='Hosting host')),
                ('is_entertainment_host', models.BooleanField(default=False, help_text='Entertainment host profile', verbose_name='Entertainment host')),
                ('is_other_services_host', models.BooleanField(default=False, help_text='Other services host profile', verbose_name='Other services host')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('entertainment_activities', models.ManyToManyField(blank=True, to='host_information.EntertainmentActivities')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('speak_languages', models.ManyToManyField(blank=True, help_text='What languages do you speak?', related_name='users', to='host_information.SpeakLanguages', verbose_name='Languages')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuarios en la plataforma',
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='EntertainmentHostProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de anfitriones de entretenimiento',
            },
        ),
        migrations.CreateModel(
            name='ExecutiveProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('occupation', models.CharField(blank=True, max_length=255, verbose_name='Occupation')),
                ('enterprise_name', models.CharField(max_length=255, verbose_name='Company to which you are linked')),
                ('companies_to_visit', models.CharField(max_length=255, verbose_name='Companies to Visit')),
                ('educational_titles', models.CharField(max_length=255)),
                ('complete_studies_school', models.CharField(max_length=255, verbose_name='Institution where completed his previous studies')),
                ('innovation_topics_choice', models.CharField(max_length=255, verbose_name='Areas of innovation of your choice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de ejecutivos',
            },
        ),
        migrations.CreateModel(
            name='HostingHostProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('stars', models.PositiveIntegerField(blank=True, help_text='Number of stars', null=True, verbose_name='Stars')),
                ('photography', models.ImageField(blank=True, null=True, upload_to='hostinghosts', verbose_name='Photo')),
                ('additional_description', models.TextField()),
                ('featured_amenities', models.ManyToManyField(help_text='What amenities do you offer?', to='host_information.FeaturesAmenities', verbose_name='Featured Amenities')),
                ('lodging_offer_type', models.ManyToManyField(help_text='What lodging offer type?', to='host_information.LodgingOfferType', verbose_name='Lodging Offer Type')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de anfitriones de hospedaje',
            },
        ),
        migrations.CreateModel(
            name='InnovationHostProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de anfitriones de innovación',
            },
        ),
        migrations.CreateModel(
            name='OtherServicesHostProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de anfitriones de servicios varios',
            },
        ),
        migrations.CreateModel(
            name='ProfessorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('occupation', models.CharField(max_length=255)),
                ('origin_education_school', models.CharField(max_length=128, verbose_name='Origin education institute')),
                ('current_education_school', models.CharField(max_length=128, verbose_name='Institution of education to which is linked in the current residence')),
                ('educational_titles', models.CharField(max_length=255)),
                ('complete_studies_school', models.CharField(max_length=255, verbose_name='Institution where completed his previous studies')),
                ('knowledge_topics_choice', models.CharField(max_length=255, verbose_name='Areas of knowledge of your choice')),
                ('research_groups', models.CharField(max_length=255, verbose_name='Research groups to which it belongs')),
                ('autorship_publications', models.CharField(max_length=255, verbose_name='Publications of its authorship')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de profesores',
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('origin_education_school', models.CharField(max_length=128, verbose_name='Origin education institute')),
                ('current_education_school', models.CharField(max_length=128, verbose_name='Institution of education to which is linked in the current residence')),
                ('extra_occupation', models.CharField(max_length=128, verbose_name='Extra occupation')),
                ('educational_titles', models.CharField(max_length=255)),
                ('complete_studies_school', models.CharField(max_length=255, verbose_name='Institution where completed his previous studies')),
                ('knowledge_topics_choice', models.CharField(max_length=255, verbose_name='Areas of knowledge of your choice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de estudiantes',
            },
        ),
        migrations.CreateModel(
            name='StudyHostProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('institution_type', models.CharField(choices=[('UNIVERSITY', 'University'), ('TECH_SCHOOL', 'Technological School'), ('UNIV_INST', 'University Institution'), ('PROF_TECH_INST', 'Professional Technological Institution'), ('CONTINUAL_EDUCATION_CENTER', 'Continual Education Center')], max_length=255, verbose_name='Institution Type')),
                ('institute_character', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public'), ('MIXED', 'Private - Public')], max_length=7, verbose_name='Character of the institution')),
                ('high_quality_accreditations', models.CharField(max_length=255, verbose_name='Accreditations of high quality')),
                ('students_number', models.CharField(choices=[('Less than a thousand students', 'Less than a thousand students'), ('Between one thousand and ten thousand students', 'Between one thousand and ten thousand students'), ('Between ten thousand and twenty thousand students', 'Between ten thousand and twenty thousand students'), ('More/Greater than twenty thousand students', 'More/Greater than twenty thousand students')], max_length=255, verbose_name='Number of students')),
                ('rankings_classification', models.CharField(max_length=255, verbose_name='Classification in ranking')),
                ('strengths', models.CharField(max_length=255, verbose_name='Strengths')),
                ('photography', models.ImageField(blank=True, null=True, upload_to='studyhosts', verbose_name='Photo')),
                ('knowledge_topics', taggit.managers.TaggableManager(help_text='A comma-separated list of topics.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Knowledge topics')),
                ('research_groups', models.ManyToManyField(help_text='What are your research groups?', to='host_information.ResearchGroups', verbose_name='Research Groups')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuarios con perfil de anfitriones de estudio',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
