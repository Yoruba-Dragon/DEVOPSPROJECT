from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name
    

class Resturant(models.Model):
    resturantname = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=250, blank=False, null=True)
    location = models.CharField(max_length=100, blank=False, null=True)
    resturant_pic = models.ImageField(upload_to='static/images/', blank=True, null=True)
    openingtime = models.TimeField(max_length=30)
    closingtime = models.TimeField(max_length=30)


    def __str__(self):
        return self.resturantname
    
class Store(models.Model):
    storename = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=250, blank=False, null=True)
    location = models.CharField(max_length=100, blank=False, null=True)
    store_pic = models.ImageField(upload_to='static/images/', blank=True, null=True)
    openingtime = models.TimeField(max_length=30)
    closingtime = models.TimeField(max_length=30)


    def __str__(self):
        return self.storename
