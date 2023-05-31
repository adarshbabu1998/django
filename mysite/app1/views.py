from django.shortcuts import render

from django.urls import path,include

urlpatterns = [
   
    path('',include('app1.urls'))
]


def home(request):
    return render(request,'home.html')


# Create your views here.

