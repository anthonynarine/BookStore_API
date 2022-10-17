from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year_published = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.IntegerField()
    
    
