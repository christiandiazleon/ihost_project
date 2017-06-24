# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0013_auto_20170622_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodgingoffer',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='studiesoffert',
            name='studies_offert_list',
        ),
        migrations.AddField(
            model_name='lodgingoffer',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
