# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='sex',
            field=models.CharField(default='', max_length=255),
        ),
    ]
