from django.db import models


class students(models.Model):
    indx=models.IntegerField()
    sname=models.CharField(max_length=20)
    scourse=models.CharField(max_length=20)


    def __str__(self):
        return self.sname

# Create your models here.
