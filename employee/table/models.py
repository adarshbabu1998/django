from django.db import models


class employee(models.Model):
    eid=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=40)


   



# Create your models here.
