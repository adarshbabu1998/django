from django.db import models


class school(models.Model):

    roll_no=models.IntegerField()
    name=models.CharField(max_length=25)
    standard=models.IntegerField()
    division=models.CharField(max_length=1)
    
class pics(models.Model):
    img=models.ImageField(upload_to="mypics/")


    def __str__(self):
        return self.name

# Create your models here.
