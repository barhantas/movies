# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 07:22
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poster_path', models.TextField(blank=True, max_length=100, null=True)),
                ('adult', models.NullBooleanField()),
                ('overview', models.TextField(blank=True, max_length=300, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('original_title', models.TextField(blank=True, null=True)),
                ('original_language', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('backdrop_path', models.TextField(blank=True, null=True)),
                ('popularity', models.TextField(blank=True, null=True)),
                ('vote_count', models.TextField(blank=True, null=True)),
                ('video', models.NullBooleanField()),
                ('vote_average', models.TextField(blank=True, null=True)),
                ('genre_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backdrop_path', models.TextField(blank=True, max_length=100, null=True)),
                ('original_title', models.TextField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, max_length=300, null=True)),
                ('runtime', models.TextField(blank=True, null=True)),
                ('vote_average', models.TextField(blank=True, null=True)),
                ('production_company', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('cast', models.CharField(blank=True, max_length=5000, null=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesAPP.Movie')),
            ],
        ),
    ]
