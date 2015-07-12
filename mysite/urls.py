from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import views

urlpatterns = patterns('',
    url(r'^$', views.RunHome.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'polls/', include('polls.urls', namespace="polls")),
)
