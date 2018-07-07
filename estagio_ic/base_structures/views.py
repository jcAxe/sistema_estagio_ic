from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'base_structures/index.html')


def about(request):
    return render(request, 'base_structures/about.html')


def student_profile(request):
    return render(request, 'base_structures/student_pages/student_profile.html')

def student_register(request):
    return render(request, 'base_structures/student_pages/student_register.html')

def student_menu(request):
    return render(request, 'base_structures/student_pages/student_menu.html')

def coordinator_profile(request):
    return render(request, 'base_structures/coordinator_pages/coordinator_profile.html')

def coordinator_register(request):
    return render(request, 'base_structures/coordinator_pages/coordinator_register.html')

def coordinator_menu(request):
    return render(request, 'base_structures/coordinator_pages/coordinator_menu.html')

def enterprise_profile(request):
    return render(request, 'base_structures/enterprise_pages/enterprise_profile.html')

def enterprise_register(request):
    return render(request, 'base_structures/enterprise_pages/enterprise_register.html')

def enterprise_menu(request):
    return render(request, 'base_structures/enterprise_pages/enterprise_menu.html')


# Create your views here.
