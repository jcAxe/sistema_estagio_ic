from django.conf.urls import url, include
from user_actions import views

urlpatterns = [

    url(r'^student_menu$', views.student_menu, name='student_menu'),
    url(r'^coordinator_menu$', views.coordinator_menu, name='coordinator_menu'),
    url(r'^enterprise_menu$', views.enterprise_menu, name='enterprise_menu'),

    url(r'^student_profile$', views.student_profile, name='student_profile'),
    url(r'^student_register$', views.student_register, name='student_register'),

    url(r'^coordinator_register$', views.coordinator_register, name='coordinator_register'),
    url(r'^enterprise_profile$', views.enterprise_profile, name='enterprise_profile'),
    url(r'^enterprise_register$', views.enterprise_register, name='enterprise_register'),

    url(r'^list_student', views.list_student, name='list_student'),
    url(r'^list_enterprise', views.list_enterprise, name='list_enterprise'),

    url(r'^validation_st/(?P<id>\d+)/(?P<student_slug>[-\w]+)/$', views.validate_student, name='validate_student'),
    url(r'^validation_ent/(?P<id>\d+)/(?P<enterprise_slug>[-\w]+)/$', views.validate_enterprise, name='validate_enterprise'),

    url(r'^successful_register/$', views.successful_register, name='successful_register'),
    url(r'^validation_result/(?P<id>\d+)/(?P<student_slug>[-\w]+)/$', views.validation_result, name='validation_result'),

]
