from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def list_job_opportunity(request):
    return render(request, 'jobs/list_job_opportunity.html')


def display_job_opportunity(request):
    return render(request, 'jobs/display_job_opportunity.html')


def list_job_application(request):
    return render(request, 'jobs/list_job_application.html')


def display_job_application(request):
    return render(request, 'jobs/display_job_application.html')

