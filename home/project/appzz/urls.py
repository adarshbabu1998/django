from django.urls import path
from . import views

urlpatterns=[
    path('' ,views.firstpage,name='firstpage'),
    path('second',views.secondpage,name='secondpage'),

]