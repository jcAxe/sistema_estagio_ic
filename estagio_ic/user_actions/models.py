from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from django.urls import reverse
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    pw = models.CharField(max_length=200)
    id_doc_number = models.PositiveIntegerField(unique=True)
    enroll_number = models.PositiveIntegerField(unique=True)
    major_id = models.PositiveIntegerField(db_index=True)
    qualifications = models.TextField(blank=True)
    gpa = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    validation_pending = models.BooleanField(default=True)
    able = models.BooleanField(default=False)
    time_available_start = models.TextField()
    time_available_end = models.TextField()

    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'student'
        verbose_name_plural = 'students'


    def recently_registred(self):
        return self.register_date >= timezone.now() - datetime.timedelta(days=1)


    #this have to be looked carefully, ass zé, trab estagio
    # def get_absolute_path(self):
    #     return reverse('user_actions:display_student', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    pw = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    validation_pending = models.BooleanField(default=True)
    able = models.BooleanField(default=False)

    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'enterprise'
        verbose_name_plural = 'enterprises'

    def recently_registred(self):
        return self.register_date >= timezone.now() - datetime.timedelta(days=1)

    # this have to be looked carefully, ass zé, trab estagio
    # def get_absolute_path(self):
    #     return reverse('user_actions:display_enterprise', args=[self.id, self.slug])

    def __str__(self):
        return self.name
