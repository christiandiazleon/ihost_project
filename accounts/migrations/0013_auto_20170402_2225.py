# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20170402_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='executiveprofile',
            name='culturals_arthistic',
            field=models.BooleanField(default=False, verbose_name='Arthistic and Culturals activities'),
        ),
        migrations.AddField(
            model_name='executiveprofile',
            name='ecological',
            field=models.BooleanField(default=False, verbose_name='Ecological activities'),
        ),
        migrations.AddField(
            model_name='executiveprofile',
            name='enterprise_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='executiveprofile',
            name='occupation',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
