from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)  # contains text format
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    discount = models.FloatField()
