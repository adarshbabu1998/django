from typing import Any
from django.db import models

# Create your models here.

class school(models.Model):
    indx = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class students(models.Model):
    roll_no = models.IntegerField()
    standard = models.SmallIntegerField()
    sname = models.CharField(max_length=20)

    def __str__(self):
        return self.sname

class category(models.Model):
    cname=models.CharField(max_length=20)

    def __str__(self):
        return self.cname
   
class product(models.Model):
    pname=models.CharField(max_length=20)
    pid=models.IntegerChoices(int )

    def __str__(self):
        return self.pname
