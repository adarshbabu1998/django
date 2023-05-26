from django.shortcuts import render


def homepage (request):
    return render (request,'homepage.html')

def welcome(request):
    return render(request,'welcome.html')


# Create your views here.
