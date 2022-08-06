from fileinput import filename
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Subcategories(models.Model):
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)

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
    information = models.TextField(max_length=1000, blank=True, null=True)
    subcategory_id = models.PositiveIntegerField(blank=True, null=True)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


# Create your models here.
