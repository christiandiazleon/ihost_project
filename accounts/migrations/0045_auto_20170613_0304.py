# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_auto_20170611_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinghostprofile',
            name='lodging_offer_type',
            field=models.CharField(choices=[('HOTEL', 'Hotel'), ('HOSTEL', 'Hostel'), ('STUDENT_RESIDENCE', 'Student Residence'), ('ACCOMODATION_WITH_LOCAL_FAMILY', 'Accommodation with local family'), ('HOUSE_APT_SHARE_VISITANTS', 'House or apartment to share with other visitors'), ('HOUSE_OR_PRIV_APT', 'House or private apartment')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studyhostprofile',
            name='photography',
            field=models.ImageField(blank=True, null=True, upload_to='studyhosts', verbose_name='Photo'),
        ),
    ]