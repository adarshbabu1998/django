from django.shortcuts import render


def homepage(request):
    return render (request,'home.html')


def add(request):
    return render (request,'add.html')


def update(request):
    return render (request,'update.html')


# Create your views here.
