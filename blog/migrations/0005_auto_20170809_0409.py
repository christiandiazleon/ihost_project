# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='article_images', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
