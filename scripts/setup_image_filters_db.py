#!/usr/bin/env python

import logging
import os
import sys

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
sys.path.insert(0, os.getcwd())
django.setup()

from imageflow.models import ImageFilter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# For nanometer ranges, see https://en.wikipedia.org/wiki/Photometric_system#Filters_used
ImageFilter.objects.create(band='B', system='Johnson', range_min_nm=442, urat1_key='Bmag').save()
ImageFilter.objects.create(band='V', system='Johnson', range_min_nm=540, urat1_key='Vmag').save()
ImageFilter.objects.create(band='g\'', system='Sloan', range_min_nm=475, urat1_key='gmag').save()
ImageFilter.objects.create(band='r\'', system='Sloan', range_min_nm=622, urat1_key='rmag').save()
ImageFilter.objects.create(band='i\'', system='Sloan', range_min_nm=763, urat1_key='imag').save()
ImageFilter.objects.create(band='J', system='2MASS', range_min_nm=1250, urat1_key='Jmag').save()
ImageFilter.objects.create(band='H', system='2MASS', range_min_nm=1650, urat1_key='Hmag').save()
ImageFilter.objects.create(band='K', system='2MASS', range_min_nm=2150, urat1_key='Kmag').save()

print 'Done.'
