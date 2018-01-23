# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-21 22:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photometry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightCurve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('image_filter', models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, related_name='lightcurve_image_filter_set', to='photometry.ImageFilter')),
                ('magband', models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, related_name='lightcurve_magband_set', to='photometry.ImageFilter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]