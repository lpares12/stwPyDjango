# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_img',
            field=models.CharField(max_length=300),
        ),
    ]
