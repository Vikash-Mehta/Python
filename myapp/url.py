#from django.contrib import admin
from django.conf.urls import patterns, include, url

#admin.autodiscover()

#urlpatterns = patterns('myapp.views',
#    url(r'^hello/', 'hello', name='hello'),
#)

urlpatterns = [
    url(r'^hello/',  'myapp.views.hello', name='hello'),
]