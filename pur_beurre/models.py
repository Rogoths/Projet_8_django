from django.db import models

# Create your models here.

class Product(models.Model):
    """table for products"""
    name = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    score = models.CharField(max_length=5)
    detail = models.CharField(max_length=400)
    ean = models.CharField(max_length=13)
