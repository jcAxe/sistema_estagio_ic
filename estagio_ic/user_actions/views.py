from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

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


def student_profile(request):
    return render(request, 'user_actions/student_pages/student_profile.html')



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




def coordinator_register(request):
    return render(request, 'user_actions/coordinator_pages/coordinator_register.html')


def enterprise_profile(request):
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

    return render(request, 'user_actions/coordinator_pages/validation_result.html', {'result': result})

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


def validate_student(request, id, student_slug):

    student = get_object_or_404(Student, id=id,
                               slug=student_slug)


    return render(request, 'user_actions/coordinator_pages/validate_student.html', {'student': student})


def validate_enterprise(request, id, enterprise_slug):

    enterprise = get_object_or_404(Enterprise, id=id,
                               slug=enterprise_slug)

    return render(request, 'user_actions/coordinator_pages/validate_enterprise.html', {'enterprise': enterprise})

# Create your views here.

