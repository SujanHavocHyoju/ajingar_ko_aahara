# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-17 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20181016_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='Category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='Location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]