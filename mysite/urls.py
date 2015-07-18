from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import views

urlpatterns = patterns('',
    url(r'^$', views.Profiles.as_view(), name='home'),
)
