# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0012_auto_20170613_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodgingoffer',
            name='birth_year',
        ),
    ]
