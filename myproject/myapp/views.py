from django.shortcuts import render
from.models  import *

def homepage(request):
    g={
        'data': vehicle.objects.all()
    }
    return render(request,'home.html',g)

def defe(request):
     s={
        'fields': pictures.objects.all()
        }
     return render(request,'defender.html',s)

def wrangler(request):
    return render(request,'wrangler.html')




# Create your views here.
