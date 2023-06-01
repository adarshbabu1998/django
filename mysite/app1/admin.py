from django.contrib import admin

from . models import school,students,category,product


# Register your models here.

admin.site.register(school) 
admin.site.register(students)  
admin.site.register(category) 
admin.site.register(product) 