# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-28 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageflow', '0026_auto_20180222_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageanalysis',
            name='image_jd_corrected',
            field=models.FloatField(null=True),
        ),
    ]
