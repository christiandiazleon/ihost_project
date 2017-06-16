# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0018_auto_20170614_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodgingoffer',
            name='room_type_offered',
            field=models.CharField(choices=[('All property', 'All property'), ('Private Room', 'Private Room'), ('Shared Room', 'Shared Room')], max_length=255, verbose_name='Room Type Offered'),
        ),
    ]