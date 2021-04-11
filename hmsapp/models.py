from django.db import models

# Create your models here.

class Student(models.Model):
    
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    #img = models.ImageField(upload_to='pics')
    enrollment = models.CharField(max_length=100)
    temperature = models.FloatField()
    oxygen = models.FloatField()
    