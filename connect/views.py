from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from connect.models import User, Lunch

def home(request): 
  return HttpResponse('Welp, hello world')

class IndexView(generic.ListView):
  template_name = 'connect/index.html'
  context_object_name = 'total_people'
  def get_queryset(self):
 return User.objects.filter(
        signup_date=timezone.now()
    ).order_by('-signup_date')[:5]

def currentWeek(request):
  # use listView template
  return HttpResponse("Current week")

def profile(request):
  # return a personal profile
  return HttpResponse('Profile Page')
