from ast import Mod
from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.IntegerField()
    
    
