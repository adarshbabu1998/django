from django.urls import path
from . import views

urlpatterns=[
    path('' ,views.home,name='home'),
    # path('second',views.secondpage,name='secondpage'),
    path('u',views.upload,name='upload')

]