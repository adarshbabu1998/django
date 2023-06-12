from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('defender',views.defe,name='defe'),
    path('wrangler',views.wrangler,name='wrangler'),
]