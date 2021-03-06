import datetime
import os
import shutil
import signal
import subprocess
import tempfile
import time

from django.shortcuts import get_object_or_404

from accounts.models import UserUploadedImage
from lightcurve.models import LightCurve
import imageflow.s3_util as s3_util

def create_new_lightcurve(user, imgs):
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    lc = LightCurve(user=user, name='%s %s' % (user.username, date))
    lc.save()

    for img in imgs:
        url = s3_util.upload_to_s3(img.read(), 'raw', img.name)
        print 'Uploaded %s to s3 url: %s' % (img.name, url)
        UserUploadedImage(user=user,
                          image_url=url,
                          original_filename=img.name,
                          lightcurve=lc).save()

    return lc

def edit_lightcurve(user, imgs, lightcurve_id):
    lc = get_object_or_404(LightCurve, id=lightcurve_id, user=user)

    for img in imgs:
        url = s3_util.upload_to_s3(img.read(), 'raw', img.name)
        print 'Uploaded %s to s3 url: %s' % (img.name, url)
        UserUploadedImage(user=user,
                          image_url=url,
                          original_filename=img.name,
                          lightcurve=lc).save()
    return lc
