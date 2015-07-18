from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class PersonalProfile(models.Model):
  first_name = models.CharField(max_length=35)
  last_name = models.CharField(max_length=35)
  status = models.IntegerField(default=0, blank=True) 
  email = models.EmailField(blank=True)
  signup_date = models.DateTimeField('date signup', blank=True) 
  user = models.ForeignKey(User, null=True)
  def __str__(self):
    return "%s %s"% (self.first_name, self.last_name)
  def resetStatus(self):
    self.status = 1   #indicates available for the week
    return "finished resetting status for the week"  

class Friendship(models.Model):
  from_friend = models.ForeignKey(
    PersonalProfile, related_name='friend_set')
  to_friend = models.ForeignKey(
    PersonalProfile, related_name='to_friend_set')
  lunch_points = models.IntegerField(default=0, blank=True)
  def __str__(self): 
    return u'%s -> %s' %(
      self.from_friend.first_name,
      self.to_friend.first_name
  )
  class Meta:
    unique_together = (('to_friend', 'from_friend'),)
  
# An instance where a few people meet
class Lunch(models.Model): 
  date = models.DateTimeField('foodie date', auto_now=True, null=True) 
  participants = models.ForeignKey(Friendship)
  def __str__(self):
    return self.date
  class Meta: 
    ordering = ('date', )
