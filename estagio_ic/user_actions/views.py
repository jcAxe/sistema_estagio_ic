from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from user_actions.models import Student
from user_actions.models import Enterprise


def student_menu(request):
    return render(request, 'user_actions/student_pages/student_menu.html')

def coordinator_menu(request):
    return render(request, 'user_actions/coordinator_pages/coordinator_menu.html')

def enterprise_menu(request):
    return render(request, 'user_actions/enterprise_pages/enterprise_menu.html')


def student_profile(request):
    return render(request, 'user_actions/student_pages/student_profile.html')


def student_register(request):
    return render(request, 'user_actions/student_pages/student_register.html')




def coordinator_register(request):
    return render(request, 'user_actions/coordinator_pages/coordinator_register.html')


def enterprise_profile(request):
    return render(request, 'user_actions/enterprise_pages/enterprise_profile.html')

def enterprise_register(request):
    return render(request, 'user_actions/enterprise_pages/enterprise_register.html')


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

