from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'base_structures/index.html')

def about(request):
    return render(request, 'base_structures/about.html')


# Create your views here.
