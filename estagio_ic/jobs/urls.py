from django.conf.urls import url, include
from jobs import views

urlpatterns = [

    url(r'^list_job_opportunity/$', views.list_job_opportunity, name='list_job_opportunity'),
    url(r'^list_job_application/$', views.list_job_application, name='list_job_application'),


    url(r'^display_job_opportunity/(?P<id>\d+)/(?P<student_slug>[-\w]+)/$', views.display_job_opportunity, name='display_job_opportunity'),

    url(r'^display_job_application/(?P<id>\d+)/$', views.display_job_application, name='display_job_application'),



]

