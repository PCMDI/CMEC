from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    data = {}
    return render(request, 'site/home.html', data)


def about(request):
    data = {}
    return render(request, 'site/about.html', data)


def ilamb(request):
    data = {}
    return render(request, 'site/ilamb.html', data)


@login_required()
def mean(request):
    data = {}
    return render(request, 'site/mean.html', data)


def pmp(request):
    data = {}
    return render(request, 'site/pmp.html', data)


def results(request):
    data = {}
    return render(request, 'site/results.html', data)


@login_required()
def variability(request):
    data = {}
    return render(request, 'site/variability.html', data)
