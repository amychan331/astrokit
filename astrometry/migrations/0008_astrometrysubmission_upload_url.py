# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrometry', '0007_astrometrysubmissionjob_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='astrometrysubmission',
            name='upload_url',
            field=models.CharField(default='n/a', max_length=512),
            preserve_default=False,
        ),
    ]
