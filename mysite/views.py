from django.http import HttpResponse,HttpResponseRedirect, HttpResponse
from polls.models import Run, Runner
from django.views import generic

class RunHome(generic.ListView):
  template_name = "mysite/home.html"
  context_object_name = 'all_runners'
  def get_queryset(self):
    return Runner.objects.all()

  
