# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

# Create your views here.
def north(request):
    return render(request, 'north.html')

def south(request):
    return render(request, 'south.html')