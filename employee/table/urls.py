from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('add',views.add,name='add'),
    path('delete/<int:s_id>',views.delete,name='delete'),
    path('edit/<int:s_id>',views.edit,name='edit'),

   
 
]