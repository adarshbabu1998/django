from django.shortcuts import render
from.models  import *

def homepage(request):
    g={
        'data': vehicle.objects.all()
    }
    return render(request,'home.html',g)

def defe(request):
    return render(request,'defender.html')




# Create your views here.
