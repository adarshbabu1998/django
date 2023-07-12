from django.shortcuts import render,redirect
from . models import *


def homepage(request):
     b={
            'save':students.objects.all()
        }
     return render (request,'home.html',b)


def add(request):
   
    if request.method=="POST":
        s=request.POST.get('No')
        n=request.POST.get('name')
        c=request.POST.get('course')
        ob=students(indx=s,sname=n,scourse=c)
        ob.save()
        return redirect(homepage)
   
    return render (request,'add.html')


def delete(request,s_id):
    delt=students.objects.get(id=s_id)
    delt.delete()
    return redirect (homepage)




def update(request):
    return render (request,'update.html')


# Create your views here.
