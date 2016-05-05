# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rater_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rater',
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
