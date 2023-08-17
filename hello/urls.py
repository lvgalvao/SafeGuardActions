from django.conf.urls import patterns, url
from .views import hello_world

urlpatterns = patterns('',
    url(r'^$', hello_world, name='hello_world'),
)
