from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('sec',views.upload,name='upload'),
    path('s',views.add,name='add'),
]