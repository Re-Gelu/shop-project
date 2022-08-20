from django.contrib import admin
from .models import *

admin.AdminSite.site_header = "Админка"
admin.AdminSite.site_title = "Админка" 

@admin.register(Main_page_slider)
class Main_page_slider_admin(admin.ModelAdmin):
    list_display = ("image", "add_date")
    list_filter = ("image", "add_date")
    search_fields = ("image__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["image"].label = "Изображение для слайдера"
        return form
    
@admin.register(Categories)
class Categories_admin(admin.ModelAdmin):
    list_display = ("name", "add_date")
    list_filter = ("name", "add_date")
    search_fields = ("name", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["name"].label = "Наименование категории"
        return form
    
@admin.register(Subcategories)
class Subcategories_admin(admin.ModelAdmin):
    list_display = ("name", "category", "add_date")
    list_filter = ("name", "category", "add_date")
    search_fields = ("name", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["name"].label = "Наименование категории"
        form.base_fields["category"].label = "Категория"
        return form
    
@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ("name", "price", "subcategory", "add_date")
    list_filter = ("name", "price")
    search_fields = ("name", )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)

        form.base_fields["name"].label = "Имя товара"

        form.base_fields["price"].label = "Цена товара"

        form.base_fields["promo_price"].label = "Цена товара со скидкой"
        form.base_fields["promo_price"].help_text = "(Опционально)"
        form.base_fields["promo_price"].required = False

        form.base_fields["image"].label = "Изображение товара"

        form.base_fields["information"].label = "Краткая информация о товаре"
        form.base_fields["information"].required = False

        form.base_fields["subcategory"].label = "Подкатегория"
        form.base_fields["subcategory"].required = False
        return form

# Register your models here.
