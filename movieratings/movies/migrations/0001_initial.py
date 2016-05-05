# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=255)),
                ('release_date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('movie_id', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movies')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Rater')),
            ],
        ),
    ]