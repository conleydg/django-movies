# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20160504_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='user_id',
            field=models.CharField(default='', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movies'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Rater'),
        ),
    ]
