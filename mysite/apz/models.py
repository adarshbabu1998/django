from django.db import models



class book(models.Model):
    title=models.CharField(max_length=30)
    pdf=models.FileField(upload_to='pages/')
    pics=models.FileField(upload_to='pics/')


# Create your models here.
