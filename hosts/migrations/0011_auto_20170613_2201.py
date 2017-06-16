# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0010_remove_lodgingoffer_lodging_offer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodgingoffer',
            name='ad_title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lodgingoffer',
            name='available_dates',
            field=models.DateField(blank=True, help_text='Days in which is possible bookings', null=True, verbose_name='Available dates'),
        ),
    ]
