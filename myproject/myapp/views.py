from django.shortcuts import render
from . models import *


def homepage(request):
    return render (request,'home.html')


def add(request):
    if request.method=="POST":
        s=request.POST.get('No')
        n=request.POST.get('name')
        c=request.POST.get('course')
        ob=students(indx=s,sname=n,scourse=c)
    
    return render (request,'add.html')


def update(request):
    return render (request,'update.html')


# Create your views here.
