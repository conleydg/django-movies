# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160505_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
    ]
