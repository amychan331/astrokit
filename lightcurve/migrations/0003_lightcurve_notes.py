# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-12 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightcurve', '0002_remove_lightcurve_image_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightcurve',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]