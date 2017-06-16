# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 04:11
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20170610_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyhostprofile',
            name='academic_mobility_programs',
        ),
        migrations.RemoveField(
            model_name='studyhostprofile',
            name='scholarships',
        ),
        migrations.RemoveField(
            model_name='studyhostprofile',
            name='studies_offert_list',
        ),
        migrations.RemoveField(
            model_name='studyhostprofile',
            name='studies_type_offered',
        ),
        migrations.AlterField(
            model_name='studyhostprofile',
            name='knowledge_topics',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of topics.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Knowledge topics'),
        ),
    ]
