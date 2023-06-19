from django.shortcuts import render,HttpResponse
from . models import school,pics


    
def firstpage(request):
    s={
        'data': school.objects.all(),
        'fields': pics.objects.all(),

    }
    return render (request,'first.html',s)
def secondpage(request):
   return render (request,'second.html')




# Create your views here.