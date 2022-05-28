from django.db import models

# Create your models here.

def size():
    return [
        ('L', 'L'),
        ('M', 'M'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]


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
    real_price = models.IntegerField()
    discount_price = models.IntegerField()

    def __str__(self):
        return self.content


class Product(models.Model):
    content = models.CharField(max_length=256)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    real_price = models.IntegerField()
    discount_price = models.IntegerField()
    image = models.ImageField()
    availibility = models.CharField(max_length=56, choices=availibility())
    rate = models.CharField(max_length=56, choices=rate())
    short_info = models.TextField()
    color = models.CharField(max_length=56)
    size = models.CharField(max_length=56, choices=size())
    description = models.TextField()

    def __str__(self):
        return self.content

