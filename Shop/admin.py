from django.contrib import admin
from .models import *

admin.AdminSite.site_header = "Админка"
admin.AdminSite.site_title = "Админка"

@admin.register(Main_page_slider)
class Main_page_slider_admin(admin.ModelAdmin):
    list_display = ("image", "updated", "created")
    list_filter = ("updated", "created")
    search_fields = ("image__startswith", )
@admin.register(Categories)
class Categories_admin(admin.ModelAdmin):
    list_display = ("name", "updated", "created")
    list_filter = ("updated", "created")
    search_fields = ("name", )
    
@admin.register(Subcategories)
class Subcategories_admin(admin.ModelAdmin):
    list_display = ("name", "category", "updated", "created")
    list_filter = ("category", "updated", "created")
    search_fields = ("name", )

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ("name", "price", "subcategory", "stock","available", "updated", "created")
    list_filter = ("subcategory", "updated", "created")
    search_fields = ("name", )
    list_editable = ('stock', 'available')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)

        form.base_fields["promo_price"].help_text = "(Опционально)"
        form.base_fields["promo_price"].required = False

        form.base_fields["information"].required = False    
        
        form.base_fields["full_information"].help_text = "(Имеется поддержка вставки HTML кода)"

        form.base_fields["stock"].required = False

        form.base_fields["subcategory"].required = False
        return form
    
@admin.register(current_orders)
class Current_orders_admin(admin.ModelAdmin):
    list_display = ("created",)
    list_filter = ("created",)
    search_fields = ("adress", )
