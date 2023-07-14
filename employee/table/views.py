from django.shortcuts import render,redirect
from .models  import *

def homepage(request):
    s={
        'item':employee.objects.all()
    }

    return render (request,'home.html',s)


def add(request):
    if request.method=='POST':
        em=request.POST.get('eid')
        ena=request.POST.get('name')
        eadd=request.POST.get('address')

        obj=employee(eid=em,name=ena,address=eadd)
        obj.save()
        return redirect(homepage)
    return render (request,'add.html')

def delete(request,s_id):
    field_del_var=employee.objects.get(id=s_id)
    field_del_var.delete()
    return redirect(homepage)

def edit(request,s_id):
    if request.method=="POST":
        no=request.POST.get('eid')
        n=request.POST.get('name')
        a=request.POST.get('address')

        employee.objects.filter(id=s_id).update(eid=no,name=n,address=a)
        return redirect(homepage)
    return render(request,'home.html',{'ed':ed})

# Create your views here.
