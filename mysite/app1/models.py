from typing import Any
from django.db import models

# Create your models here.

class school(models.Model):
    indx = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
   