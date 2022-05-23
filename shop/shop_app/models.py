from django.db import models

# Create your models here.


def availibility():
    return [
        ('In Stock', 'In Stock'),
        ('In Cash', 'In Cash'),
        ('By Credit Card', 'By Credit Card'),
    ]


def rate():
    return [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    ]


def price():
    return [
        ('$', '$'),
        ('€', '€'),
        ('UZS', 'UZS'),
    ]


class Category(models.Model):
    image = models.ImageField()
    content = models.CharField(max_length=100)
    price_symbol = models.CharField(max_length=56, choices=price())
    price = models.IntegerField()


class Product(models.Model):
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    availibility = models.CharField(max_length=56, choices=availibility())
    rate = models.CharField(max_length=56, choices=rate())
    short_info = models.TextField()
    color = models.CharField(max_length=56)
    size = models.CharField
    description = models.TextField()


