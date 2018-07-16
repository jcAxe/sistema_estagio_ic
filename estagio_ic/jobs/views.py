from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from jobs.models import JobOpportunity, Application


def list_job_opportunity(request):
    job_opportunities = JobOpportunity.objects.filter(available=True)


    return render(request, 'jobs/list_job_opportunity.html', {
        'job_opportunities' : job_opportunities,
        })

def display_job_opportunity(request, id, opportunity_slug):

    job_opportunity = get_object_or_404(JobOpportunity, id=id,
                                        slug=opportunity_slug)

    return render(request, 'jobs/display_job_opportunity.html', {
        'job_opportunity' : job_opportunity,
        })


def list_job_application(request):
    verified_applications = Application.objects.filter(selected=True, verified=True)
    unverified_applications = Application.objects.filter(selected=True, verified=False)

    return render(request, 'jobs/list_job_applications.html', {
        'verified_applications' : verified_applications,
        'unverified_applications' : unverified_applications,
        })


def display_job_application(request, id):

    application = get_object_or_404(Application, id=id)

    return render(request, 'jobs/display_job_application.html', {
        'application' : application,
        })

def approve_application(request, id):
    application = get_object_or_404(Application, id=id)

    application.verified = True
    application.approved = True
    application.save()
    result = application.approved

    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})

def disapprove_application(request, id):
    application = get_object_or_404(Application, id=id)

    application.verified = True
    application.approved = False
    application.save()
    result = application.approved

    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})



    