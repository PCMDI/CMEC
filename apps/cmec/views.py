# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


def home(request):
    data = {}
    return render(request, 'site/home.html', data)
