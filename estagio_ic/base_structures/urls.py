from django.conf.urls import url, include
from django.contrib import admin
from base_structures import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^student_profile$', views.student_profile, name='student_profile'),
    url(r'^student_register$', views.student_register, name='student_register'),
    url(r'^student_menu$', views.student_menu, name='student_menu'),
    url(r'^coordinator_profile$', views.coordinator_profile, name='coordinator_profile'),
    url(r'^coordinator_register$', views.coordinator_register, name='coordinator_register'),
    url(r'^coordinator_menu$', views.coordinator_menu, name='coordinator_menu'),
    url(r'^enterprise_profile$', views.enterprise_profile, name='enterprise_profile'),
    url(r'^enterprise_register$', views.enterprise_register, name='enterprise_register'),
    url(r'^enterprise_menu$', views.enterprise_menu, name='enterprise_menu'),

]
