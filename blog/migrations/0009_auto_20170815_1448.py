# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170810_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('updated',)},
        ),
    ]
