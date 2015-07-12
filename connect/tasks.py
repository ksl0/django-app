from __future__ import absolute_import
from celery import task
from connect.models import User, Lunch
from django.utils import timezone

from django.core.mail import send_mail
## Weekly tasks that where you pair up each person with another

### Friend list documentation
## -1 indicated that the friend is inactive
## 0 available, not yet dined with yet 
## +1 for each time they eat with eachother  

@task(name='tasks.add')
def add(x,y):
  print("Running periodic task!")
  return x+y

@task(name='task.spam_email'):
  send_mail('terminal!!', "message: yay celery!!", 'biking.cactus@gmail.com',['nutella164@gmail.com'], fail_silently=False)
  print("email sent!")
  


