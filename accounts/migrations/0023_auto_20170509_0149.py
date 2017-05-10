# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_professorprofile_autorship_publications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professorprofile',
            name='entertainment_activities_choice',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='entertainment_activities_choice',
        ),
        migrations.AddField(
            model_name='executiveprofile',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, verbose_name='Occupation'),
        ),
        migrations.AddField(
            model_name='user',
            name='entertainment_activities_choice',
            field=models.CharField(default=1, max_length=255, verbose_name='Entertainment activities of your choice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='executiveprofile',
            name='enterprise_name',
            field=models.CharField(max_length=255, verbose_name='Company to which you are linked'),
        ),
    ]
