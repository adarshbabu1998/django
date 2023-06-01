from django.shortcuts import render
from . models import school,students


def home(request):
    d={
        'sdata': school.objects.all(),
        'sstudents':students.objects.all()
    }
    return render(request,'home.html',d)


# Create your views here.

