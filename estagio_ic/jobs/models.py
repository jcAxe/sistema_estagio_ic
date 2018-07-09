from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from django.urls import reverse
from django.utils import timezone
from user_actions.models import Student
from user_actions.models import Enterprise

class JobOpportunity (models.Model):
    name = models.CharField(max_length=200, db_index=True)
    enterprise = models.ForeignKey(Enterprise, related_name='owner')

    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    salary = models.PositiveIntegerField(unique=True)

    weekly_workload = models.TextField(blank=True)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'job_opportunity'
        verbose_name_plural = 'job_opportunities'


    def recently_registred(self):
        return self.register_date >= timezone.now() - datetime.timedelta(days=1)


    #this have to be looked carefully, ass zé, trab estagio
    def get_absolute_path(self):
        return reverse('jobs:display_job_opportunity', args=[self.id, self.slug])

    def __str__(self):
        return self.name

class Application (models.Model):
    student_cpf = models.ForeignKey(Student, related_name='applicant')
    job_opportunity = models.ForeignKey(JobOpportunity, related_name='related_opportunity')

    application_date = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False)

    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('application_date',)
        verbose_name = 'application'
        verbose_name_plural = 'applications'


    def recently_registred(self):
        return self.register_date >= timezone.now() - datetime.timedelta(days=1)


    #this have to be looked carefully, ass zé, trab estagio
    # def get_absolute_path(self):
    #     return reverse('user_actions:display_student', args=[self.id, self.slug])

    def __str__(self):
        return 'candidatura_' + self.id
