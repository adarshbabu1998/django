from django.db import models
class vehicle(models.Model):
    veh=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    indx=models.IntegerField()
# Create your models here.
