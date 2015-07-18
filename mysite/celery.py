from __future__ import absolute_import

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from django.conf import settings
 
# get the environment variables from Heroku
#import settings to run locally
app = Celery('mysite', 
  BROKER_URL=os.environ['REDIS_URL'],
  CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

try:
  from .local_settings import *
except ImportError:
  pass

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.CELERY_TIMEZONE = 'US/Eastern'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
