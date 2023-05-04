from django.db import models

# Create your models here.
class task(models.Model):
    index =models.IntegerField(max_length=5)
    task1 = models.CharField(max_length=100)