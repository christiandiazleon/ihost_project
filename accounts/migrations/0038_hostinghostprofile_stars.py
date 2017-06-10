# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20170608_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinghostprofile',
            name='stars',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='Number of stars', verbose_name='Stars'),
            preserve_default=False,
        ),
    ]
