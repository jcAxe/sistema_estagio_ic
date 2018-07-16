from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from jobs.models import JobOpportunity


def list_job_opportunity(request):
    job_opportunities = JobOpportunity.objects.filter(available=True)


    return render(request, 'jobs/list_job_opportunity.html', {
        'job_opportunities' : job_opportunities,
        })

def display_job_opportunity(request, id, student_slug):

    job_opportunity = get_object_or_404(JobOpportunity, id=id,
                                        slug=student_slug)

    return render(request, 'jobs/display_job_opportunity.html', {
        'job_opportunity' : job_opportunity,
        })


def list_job_application(request):
    return render(request, 'jobs/list_job_application.html')


def display_job_application(request):
    return render(request, 'jobs/display_job_application.html')

