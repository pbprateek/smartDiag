# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-07-26 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('iname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LiverPatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('total_bilirubin', models.FloatField()),
                ('direct_bilirubin', models.FloatField()),
                ('alkaline_phosphotase', models.FloatField()),
                ('alamine_aminotransferase', models.FloatField()),
                ('aspartate_aminotransferase', models.FloatField()),
                ('total_proteins', models.FloatField()),
                ('albumin', models.FloatField()),
                ('albuminGlobulin_ratio', models.FloatField()),
                ('hasDisease', models.IntegerField()),
            ],
        ),
    ]
