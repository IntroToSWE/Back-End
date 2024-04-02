from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# database table for personal plants
class personalPlant(models.Model):
    # attributes
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    plantID = models.ForeignKey("libraryPlant", on_delete=models.CASCADE) # we can use this ID to reference the plant info in sep. table
    alive = models.BooleanField(default=False)
    # name = models.CharField(max_length=200)
    # size = models.CharField(max_length=50)
    # description = models.TextField(null=True, blank=True)
    # inside = models.BooleanField(default=True)
    # water = models.CharField(max_length=200)
    # sun = models.CharField(max_length=200)
    # fertilization= models.CharField(max_length=200)
    # soil = models.CharField(max_length=200)
    # alive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'base'


# databse for plant library 
class libraryPlant(models.Model):
    # id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
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

    class Meta:
        app_label = 'base'

    def __str__(self):
        return self.name

class Users(models.Model):
    # id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=75, blank=True, default='')
    last_name = models.CharField(max_length=75, blank=True, default='')
    email = models.EmailField(max_length=150, blank=True, default='', unique=True)
    password = models.CharField(max_length=50, default='', null=False)


