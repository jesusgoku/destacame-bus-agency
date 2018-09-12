# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 17:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=10, verbose_name='Capacity')),
                ('identifier', models.CharField(max_length=255, unique=True, verbose_name='Identifier')),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Bus', verbose_name='Bus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Driver', verbose_name='Driver')),
            ],
            options={
                'verbose_name': 'Itinerary',
                'verbose_name_plural': 'Itineraries',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Position')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone')),
                ('emergency_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Emergency name')),
                ('emergency_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Emergency phone')),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Itinerary', verbose_name='Itinerary')),
            ],
            options={
                'verbose_name': 'Passenger',
                'verbose_name_plural': 'Passengers',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('duration', models.FloatField(blank=True, null=True, verbose_name='Duration')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.AddField(
            model_name='itinerary',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Route', verbose_name='Route'),
        ),
    ]
