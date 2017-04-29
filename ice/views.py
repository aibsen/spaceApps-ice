# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import h5py
def index(request):
    fileName = "ice/data/ATM_dense_point_cloud/2013.03.20/ILATM1B_20130320_141441.ATM4BT4.h5"
    f = h5py.File(fileName,  "r")
    for item in f.attrs.keys():
        print item + ":", f.attrs[item]
    f.close()
    return render(request, 'index.html')


# Create your views here.
def north(request):
    return render(request, 'north.html')

def south(request):
    return render(request, 'south.html')
