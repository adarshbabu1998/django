from django.shortcuts import render,redirect
from . models import *
from.forms import bookform


def upload(request):
    form=bookform()
    if (request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'files.html',{"form":form})
def home(request):
    b={
        'dwnl':book.objects.all()
    }

    return render(request,'first.html',b)

    
# def firstpage(request):
#     s={
#         'data': school.objects.all(),
#         'fields': pics.objects.all(),

#     }
#     return render (request,'first.html',s)
# def secondpage(request):
#    return render (request,'second.html')




# Create your views here.