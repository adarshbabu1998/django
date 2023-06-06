from django.shortcuts import render
from.models import *

# Create your views here.
def homepage(request):
    return render (request,'home.html')


def contact(request):
    g={
        'fields': pictures.objects.all()

    }
    return render (request,'contact.html',g)


def about(request):
    return render (request,'about.html')
