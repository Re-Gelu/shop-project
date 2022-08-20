from unicodedata import category
from django.utils import timezone
from django.db import models

import datetime

class Categories(models.Model):
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Subcategories(models.Model):
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Main_page_slider(models.Model):
    image = models.ImageField(upload_to="main_page_slider")
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promo_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="product_images")
    information = models.TextField(max_length=100, blank=True, null=True)
    add_date = models.DateTimeField(auto_now=True)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name
    
    def was_publiched_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=7)
    


# Create your models here.
