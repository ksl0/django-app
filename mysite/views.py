from django.http import HttpResponse,HttpResponseRedirect, HttpResponse
from connect.models import PersonalProfile 
from django.views import generic

class Profiles(generic.ListView):
  template_name = "mysite/home.html"
  context_object_name = 'all_runners'
  def get_queryset(self):
    return PersonalProfile.objects.all()

  
