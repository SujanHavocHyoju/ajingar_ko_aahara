# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-17 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20181017_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='timestamp',
            new_name='added_date',
        ),
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='updated',
            new_name='updated_date',
        ),
    ]
