"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
## some import errors?
from __future__ import absolute_import


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_!6y6(_1q*sv&q7!ym&^+upe=7y6@^yfh0=i^2blpbe6s@xi9x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery', 
    'geoposition',   
    'connect', 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]


## settings for deploying
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


try:
  from .local_settings import *
except ImportError:
  pass


# CELERY SETTINGS
BROKER_URL = 'redis://h:pbtcgkislmiikl1e25t5smgi2uo@ec2-54-83-57-64.compute-1.amazonaws.com:7909'
CELERY_RESULT_BACKEND = 'redis://h:pbtcgkislmiikl1e25t5smgi2uo@ec2-54-83-57-64.compute-1.amazonaws.com:7909'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {  #add every minute
   # Executes every minutes to show that celery is working
   'send-more-mail':{
     'task': 'task.spam_email', 
     'schedule': crontab(hour='*/1'),
   },
   'saturday-reset-weekly-availibility':{
     #Executes every Saturday night at 11:59 P.M.
     'task': 'task.reset_weekly_avail' ,
     'schedule': crontab(hour=23, minute=59, day_of_week=6),
   },
   'create-weekly-lunch-schedule':{
     # Executes each Sunday at noon
     'task': 'task.weekly_lunch_setup',
     'schedule': crontab(hour=12, minute=0, day_of_week=0),
   }, 
}

## email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'biking.cactus@gmail.com'
EMAIL_HOST_PASSWORD = 'testEmail'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL= EMAIL_HOST_USER

