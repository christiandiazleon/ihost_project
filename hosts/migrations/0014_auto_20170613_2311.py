# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 23:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosts', '0013_remove_lodgingoffer_birth_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodgingoffer',
            name='hosting_host_user',
        ),
        migrations.AddField(
            model_name='lodgingoffer',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studiesoffert',
            name='ad_title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
