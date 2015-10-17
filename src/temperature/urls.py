from django.conf.urls import patterns, url
from temperature import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^save_temp_reading$', views.save_temp_reading, name='save_temp_reading'),
        )
