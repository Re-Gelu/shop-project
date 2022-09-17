from tabnanny import verbose
from django.utils import timezone
from django.db import models
from django.urls import reverse
import datetime

class Categories(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование категории"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления категории"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления категории"
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Subcategories(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование подкатегории"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления подкатегории"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления подкатегории"
    )
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'подкатегорию'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
    
class Main_page_slider(models.Model):
    image = models.ImageField(
        upload_to="main_page_slider", verbose_name="Изображение"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления изображения"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления изображения"
    )
    class Meta:
        verbose_name = 'изображение в слайдере'
        verbose_name_plural = 'Изображения в слайдере'

    def __str__(self):
        return str(self.image)

class Products(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование товара"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена товара"
    )
    promo_price = models.DecimalField(
        max_digits=10, decimal_places=2, 
        blank=True, null=True, verbose_name="Цена товара со скидкой"
    )
    image = models.ImageField(
        upload_to="product_images", verbose_name="Изображение товара"
    )
    information = models.TextField(
        max_length=100, blank=True, null=True, 
        verbose_name="Краткая информация о товаре"
    )
    full_information = models.TextField(
        max_length=1000, blank=True, null=True,
        verbose_name="Полная информация о товаре"
    )
    stock = models.PositiveIntegerField(
        verbose_name="Остаток товара"
    )
    available = models.BooleanField(
        default=True, verbose_name="Наличие товара"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления товара"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления товара"
    )
    subcategory = models.ForeignKey(
        Subcategories, on_delete=models.CASCADE, blank=True, 
        null=True, verbose_name="Подкатегория товара"
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self):
        return self.name
    
    def was_publiched_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)
    
    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.available = False
        super(Products, self).save(*args, **kwargs)

class current_orders(models.Model):
    
    order_UUID =  models.UUIDField(auto_created=True)
    
    product_list = models.TextField(
        blank=True, null=True,
        verbose_name="Список товаров",
        editable=False
    )
    
    adress = models.TextField(
        blank=True, null=True,
        verbose_name="Адрес клиента",
        editable=False
    )
    
    contacts = models.TextField(
        blank=True, null=True,
        verbose_name="Контакты клиента",
        editable=False
    )
    
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания заказа"
    )

    def expire_time(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)
    
    def __str__(self):
        return self.adress
    
    class Meta:
        verbose_name = 'текущий заказ'
        verbose_name_plural = 'Текущие заказы'