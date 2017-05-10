# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 03:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20170419_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Required. Letters, digits and @/./+/-/_ only.', max_length=254, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid email address.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='speak_languages',
            field=models.CharField(choices=[('SPA', 'Spanish'), ('ENG', 'English'), ('DEU', 'German'), ('FRA', 'French'), ('POR', 'Portuguese')], max_length=255),
        ),
    ]