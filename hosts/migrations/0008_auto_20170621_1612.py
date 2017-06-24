# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0007_auto_20170621_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodgingoffer',
            name='bed_type',
            field=models.CharField(choices=[('Single bed', 'Single bed'), ('Double bed', 'Double bed')], max_length=10, verbose_name='Bed type'),
        ),
    ]
