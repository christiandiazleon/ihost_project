# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 22:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntertainmentActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Entertainment Activities',
                'verbose_name_plural': 'Entertainment Activities',
            },
        ),
        migrations.CreateModel(
            name='FeaturesAmenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'What amenities do you offer?',
                'verbose_name_plural': 'What amenities do you offer?',
            },
        ),
        migrations.CreateModel(
            name='LodgingOfferType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Lodging Offer Type',
                'verbose_name_plural': 'Lodging Offer Type',
            },
        ),
        migrations.CreateModel(
            name='LodgingServiceOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Offered Services',
                'verbose_name_plural': 'Offered Services',
            },
        ),
        migrations.CreateModel(
            name='ResearchGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Research Groups',
                'verbose_name_plural': 'Research Groups',
            },
        ),
        migrations.CreateModel(
            name='RoomInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Room caracteristics',
                'verbose_name_plural': 'Room caracteristics',
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('who_can_apply', models.TextField()),
                ('application_process', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Scholarship',
                'verbose_name_plural': 'Scholarships',
            },
        ),
        migrations.CreateModel(
            name='SpeakLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Speak Language',
                'verbose_name_plural': 'Speak Languages',
            },
        ),
    ]
