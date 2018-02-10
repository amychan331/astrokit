# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-10 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageflow', '0011_reduction_tf_std'),
    ]

    operations = [
        migrations.AddField(
            model_name='reduction',
            name='hidden_transform',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='reduction',
            name='hidden_transform_graph_url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='reduction',
            name='hidden_transform_rval',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='reduction',
            name='hidden_transform_std',
            field=models.FloatField(null=True),
        ),
    ]
