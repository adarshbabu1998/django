from django.db import models



class book(models.Model):
    title=models.CharField(max_length=30)
    pdf=models.FileField(upload_to='pages/')
    pics=models.FileField(upload_to='pics/')




class formdata(models.Model):
    uname=models.CharField(max_length=20)
    em=models.EmailField(max_length=20)
    feedback=models.CharField(max_length=20)


# Create your models here.
