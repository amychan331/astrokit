# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-19 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imageflow', '0004_imageanalysis_uploaded_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reduction',
            name='analysis',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='analysis', to='imageflow.ImageAnalysis'),
        ),
    ]
