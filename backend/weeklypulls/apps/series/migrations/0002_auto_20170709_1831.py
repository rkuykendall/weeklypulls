# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-09 18:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='read',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='series',
            name='skipped',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
    ]
