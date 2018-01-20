import datetime
import os
import shutil
import signal
import subprocess
import tempfile
import time

from django.conf import settings

from astrometry.astrometry_client import Client
from astrometry.models import AstrometrySubmission
from imageflow.models import UserUploadedImage
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

def process_astrometry_online(url):
    '''
    Uses astrometry.net to fetch astrometry info.
    '''

    client = Client()
    client.login(settings.ASTROKIT_ASTROMETRY_KEY)
    result = client.url_upload(url)
    success = result['status'] == 'success'
    if success:
        astrometry_submission = AstrometrySubmission.objects.create(
                subid=result['subid'], upload_url=url)
    else:
        astrometry_submission = AstrometrySubmission.objects.create(
                subid=result['subid'],
                upload_url=url,
                status=AstrometrySubmission.FAILED_TO_SUBMIT)
    return astrometry_submission

def process_astrometry_locally(image_data):
  '''
  Returns astrometry data for a given sky image.
  '''

  with tempfile.NamedTemporaryFile(prefix='astrometry_', delete=False) as f:
      f.write(image_data)
      f.flush()
      print f.name

      output_dir = tempfile.mkdtemp(prefix='astrometry_results_')
      print output_dir

      result = _timeout_command('solve-field --no-plots --cpulimit 30 -o solution --scale-units degwidth --scale-low 0 --scale-high 2 %s -D %s' \
          % (f.name, output_dir), 60)
  return result

def _timeout_command(command, timeout):
  """
  Call shell command and either return its output or kill it
  if it doesn't normally exit within timeout seconds and return None
  """
  start = datetime.datetime.now()
  process = subprocess.Popen(command, stdout=subprocess.PIPE, \
      stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
  while process.poll() is None:
    time.sleep(0.1)
    now = datetime.datetime.now()
    if (now - start).seconds > timeout:
      os.killpg(process.pid, signal.SIGTERM)
      os.waitpid(-1, os.WNOHANG)
      return None
  return process.stdout.read()
