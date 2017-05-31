# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_information', '0004_featuresamenities_lodgingserviceoffer'),
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodgingoffer',
            name='featured_amenities',
            field=models.ManyToManyField(help_text='What amenities do you offer?', to='host_information.FeaturesAmenities', verbose_name='Featured Amenities'),
        ),
        migrations.AddField(
            model_name='lodgingoffer',
            name='offered_services',
            field=models.ManyToManyField(help_text='What services do you offer?', to='host_information.LodgingServiceOffer', verbose_name='Offered Services'),
        ),
    ]
