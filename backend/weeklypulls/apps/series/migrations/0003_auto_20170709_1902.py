# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-09 19:02
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20170709_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='read',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='series',
            name='skipped',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
    ]
