from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from jobs.models import JobOpportunity, Application
from user_actions.models import Student
from user_actions.models import Enterprise
from user_actions.forms import StudentRegisterForm
from user_actions.forms import EnterpriseRegisterForm

def student_menu(request):
    return render(request, 'user_actions/student_pages/student_menu.html')

def coordinator_menu(request):
    return render(request, 'user_actions/coordinator_pages/coordinator_menu.html')

def enterprise_menu(request):
    return render(request, 'user_actions/enterprise_pages/enterprise_menu.html')


def student_profile(request, id):
    student = get_logged_student()
    name = student.name
    enroll = student.enroll
    description = student.description
    return render(request, 'user_actions/student_pages/student_profile.html', {'name' : name,
                                                                                'enroll':enroll,
                                                                                'description':description})



def student_register(request):

    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)

        if form.is_valid():
            preview = form.save(commit=False)
            preview.slug = slugify(preview.name)
            preview.save()
            return HttpResponseRedirect(reverse('user_actions:successful_register'))
    else:
        form = StudentRegisterForm()



    return render(request, 'user_actions/student_pages/student_register.html',{'form' : form})


def student_login(request):
    try:
        student = get_logged_student()
    except Student.DoesNotExist:
        return render(request, 'user_actions/student_pages/student_login.html')
    return render(request, 'user_actions/student_pages/student_profile.html', {'student' : student})

def enterprise_login(request):
    try:
        enterprise = get_logged_enterprise()
    except Enterprise.DoesNotExist:
        return render(request, 'user_actions/enterprise_pages/enterprise_login.html')
    return render(request, 'user_actions/enterprise_pages/enterprise_profile.html', {'enterprise' : enterprise})

def student_auth(request):
    cpf = request.POST.get('id')
    password = request.POST.get('password')
    student = Student.objects.get(id_doc_number=cpf)
    if student.pw == password:
        student.logged = True
        student.save()
        student = get_logged_student()
        return render(request, 'user_actions/student_pages/student_profile.html', {'student' : student})
    else:
        return render(request, 'user_actions/student_pages/student_login.html')


def enterprise_auth(request):
    cnpj = request.POST.get('id')
    password = request.POST.get('password')
    enterprise = Enterprise.objects.get(id=cnpj)
    if enterprise.pw == password:
        enterprise.logged = True
        enterprise.save()
        enterprise = get_logged_enterprise()
        return render(request, 'user_actions/enterprise_pages/enterprise_profile.html', {'enterprise' : enterprise})
    else:
        return render(request, 'user_actions/enterprise_pages/enterprise_login.html')



def coordinator_register(request):
    return render(request, 'user_actions/coordinator_pages/coordinator_register.html')


def enterprise_profile(request):
    enterprise = get_logged_enterprise()

    return render(request, 'user_actions/enterprise_pages/enterprise_profile.html')

def enterprise_register(request):
    if request.method == 'POST':
        form = EnterpriseRegisterForm(request.POST)

        if form.is_valid():
            preview = form.save(commit=False)
            preview.slug = slugify(preview.name)
            preview.save()
            return HttpResponseRedirect(reverse('user_actions:successful_register'))
    else:
        form = EnterpriseRegisterForm()

    return render(request, 'user_actions/enterprise_pages/enterprise_register.html',{'form' : form})


def successful_register(request):
    return render(request, 'user_actions/successful_register.html')


def validation_result(request, id, student_slug):

    student = get_object_or_404(Student, id=id,
                               slug=student_slug)

    result = student.registered
    print(result)
    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})



def approve_student(request, id, student_slug):
    student = get_object_or_404(Student, id=id,
                                slug=student_slug)

    student.registered = True
    student.validation_pending = False
    student.save()
    result = student.registered

def disapprove_student(request, id, student_slug):
    student = get_object_or_404(Student, id=id,
                                slug=student_slug)
    student.registered = False
    student.validation_pending = False
    student.save()
    result = student.registered

    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})


def approve_enterprise(request, id, enterprise_slug):
    enterprise = get_object_or_404(Enterprise, id=id,
                                slug=enterprise_slug)

    enterprise.registered = True
    enterprise.validation_pending = False
    enterprise.save()
    result = enterprise.registered

    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})

def disapprove_enterprise(request, id, enterprise_slug):
    enterprise = get_object_or_404(Enterprise, id=id,
                                slug=enterprise_slug)
    enterprise.registered = False
    enterprise.validation_pending = False
    enterprise.save()
    result = enterprise.registered

    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})


def list_student(request):

    unverified_students = Student.objects.filter(validation_pending=True)
    verified_students = Student.objects.filter(validation_pending=False)


    return render(request, 'user_actions/coordinator_pages/list_student.html', {
        'unverified_students' : unverified_students,
        'verified_students' : verified_students,
        })



def list_enterprise(request):
    unverified_enterprises = Enterprise.objects.filter(validation_pending=True)
    verified_enterprises = Enterprise.objects.filter(validation_pending=False)


    return render(request, 'user_actions/coordinator_pages/list_enterprise.html', {
        'unverified_enterprises' : unverified_enterprises,
        'verified_enterprises' : verified_enterprises,
        })

def list_candidates(request):

    logged_enterprise = get_logged_enterprise()
    job_opportunites = JobOpportunity.objects.all()
    for opportunity in job_opportunites:
        if opportunity.enterprise.id == logged_enterprise.id:
            company_opportunites = opportunity

    applications = Application.objects.all()
    valid_applications = []

    for application in applications:
        if application.job_opportunity.id == company_opportunites.id:
            valid_applications.append(application)


    return render(request, 'user_actions/enterprise_pages/list_candidates.html', {
        'valid_applications' : valid_applications,
        })



def validate_student(request, id, student_slug):

    student = get_object_or_404(Student, id=id,
                               slug=student_slug)


    return render(request, 'user_actions/coordinator_pages/validate_student.html', {'student': student})


def validate_enterprise(request, id, enterprise_slug):

    enterprise = get_object_or_404(Enterprise, id=id,
                               slug=enterprise_slug)

    return render(request, 'user_actions/coordinator_pages/validate_enterprise.html', {'enterprise': enterprise})


def get_logged_student():
    logged_student = Student.objects.get(logged=True)
    return logged_student

def get_logged_enterprise():
    logged_enterprise = Enterprise.objects.get(logged=True)
    return logged_enterprise

# Create your views here.

