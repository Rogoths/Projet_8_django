from django.db import models

# Create your models here.



class Product(models.Model):
    """table for products"""
    name = models.CharField(max_length=200)
    score = models.CharField(max_length=1)
    categorie = models.ForeignKey('Categories', on_delete=models.CASCADE,)
    fat = models.FloatField(max_length=5, default=0)
    sugar = models.FloatField(max_length=5, default=0)
    salt = models.FloatField(max_length=5, default=0)
    detail = models.CharField(max_length=400)
    ean = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class Categories(models.Model):
    """table for categories"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Favoris(models.Model):
    pass
