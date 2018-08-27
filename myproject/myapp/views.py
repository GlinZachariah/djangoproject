# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context ={
        'title': 'App1'
    }
    return render(request,'index.html',context)

