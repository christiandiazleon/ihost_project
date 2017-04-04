# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20170404_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainmenthostprofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='hostinghostprofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='innovationhostprofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='otherserviceshostprofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='studyhostprofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
