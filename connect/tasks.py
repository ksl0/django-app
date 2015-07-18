from __future__ import absolute_import
from celery import task
from connect.models import PersonalProfile, Lunch
from django.utils import timezone

from django.core.mail import send_mail
from django.db.models import Q #used for queries in django

## Weekly tasks that where you pair up each person with another
### Friend list documentation
## 1 available, not yet dined with yet 
## 0 for unavailable
## +1 for each time they eat with eachother  
# Based on the connectivity indicator, lunch_points, and their 
# availability, return a candidate for lunch with input value 'person'
def choosePartner(person): 
  choices = person.friend_set.all().filter(~Q(to_friend__status = 0)).order_by('lunch_points')[:5]  #new people have lunch together
  return choices[0] #get the first person
 
   
@task(name='task.weekly_lunch_setup') 
def setUpLunch():
  list_persons = PersonalProfile.objects.all()
  for person in list_persons:
    if person.status == 1: #only setup lunch if they are available
      lunch_mate = choosePartner(person)
      #record both directions of friendship
      friendship = Friendship.objects.get(Q(from_friend = person) \
                                            & Q(to_friend=lunch_mate))
      mirror_friendship= Friendship.objects.get(Q(to_friend = person) \
                                            & Q(from_friend=lunch_mate))

      # update their availability 
      lunch_mate.resetStatus()
      person.resetStatus()
      #increment friendship strength
      friendship.lunch_points = friendship.lunch_points + 10
      mirror_friendship.lunch_points = mirror_friendship.lunch_points + 10
      #add an instance of their lunch in history
      l = Lunch(participants=friendship, date = timezone.now()); 
      l.save()
  return 0  

## resets the lunch points for the week
## TODO: ensure runs at different time than setUpLunch (or runs right after)
@task(name='task.reset_weekly_avail')
def resetStatus():
  list_persons = PersonalProfile.objects.all().map(lambda u: u.resetStatus())

#####################
#Test functions, indicating celery functionality
@task(name='task.spam_email')
def spam_email():
  send_mail('terminal!!', "message: yay celery!!", \
            'biking.cactus@gmail.com',['biking.cactus@gmail.com'], \
             fail_silently=False)
  print("email sent!")
