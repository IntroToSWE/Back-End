from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# database table for personal plants
class personalPlant(models.Model):
    # attributes
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    inside = models.BooleanField(default=True)
    water = models.CharField(max_length=200)
    sun = models.CharField(max_length=200)
    fertilization= models.CharField(max_length=200)
    soil = models.CharField(max_length=200)
    alive = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# databse for plant library 
class libraryPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    size = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    inside = models.BooleanField(default=True)
    water = models.CharField(max_length=200)
    sun = models.CharField(max_length=200)
    fertilization= models.CharField(max_length=200)
    soil = models.CharField(max_length=200)
    pet = models.BooleanField(default=False)

    def __str__(self):
        return self.name



