from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from user_actions.models import Student
from user_actions.models import Enterprise

def index(request):
    return render(request, 'base_structures/index.html')

def about(request):
    return render(request, 'base_structures/about.html')

def logout(request):
    all_students = Student.objects.all()
    all_students.update(logged = False)

    all_enterprise = Enterprise.objects.all()
    all_enterprise.update(logged = False)

    return render(request, 'base_structures/index.html')


# Create your views here.
