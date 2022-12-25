from django.contrib import admin
from django.utils.html import format_html
from extra_settings.models import Setting
from filebrowser.base import FileObject
import filebrowser
from django.conf import settings
from allauth.account.models import EmailAddress
from .models import *

admin.site.unregister(EmailAddress)
Setting._meta.verbose_name = "настройку"
Setting._meta.verbose_name_plural = "Настройки"

#admin.AdminSite.site_header = "Админка"
#admin.AdminSite.site_title = "Админка"


class SubcategoriesInline(admin.TabularInline):
    model = Subcategories

@admin.register(MainPageSlider)
class MainPageSliderAdmin(admin.ModelAdmin):
    list_display = ("image", "updated", "created")
    list_filter = ("updated", "created")
    search_fields = ("image__startswith", )
    
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "updated", "created")
    list_filter = ("updated", "created")
    search_fields = ("name", )
    inlines = [
        SubcategoriesInline,
    ]
    
@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "updated", "created")
    list_filter = ("category", "updated", "created")
    search_fields = ("name", )

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "image_tag", "price", "subcategory", "stock","available", "updated", "created")
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
    
    def image_tag(self, obj):
        if obj.image != '#':
            obj = FileObject(f"{settings.BASE_DIR}{obj.image.url}")
            return format_html(f'<img src="{obj.version_generate("admin_thumbnail").url}"/>')
        else:
            return format_html(f'<img src="#"/>')
    
    image_tag.short_description = "Изображение товара"
    