# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_studiesoffert_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studiesoffert',
            name='accreditations',
        ),
    ]
