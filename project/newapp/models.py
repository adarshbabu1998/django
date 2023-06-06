from django.db import models

# Create your models here.
class pictures(models.Model):
    p=models.ImageField(upload_to="mypics/")