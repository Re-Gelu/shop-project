from django.contrib import admin
from .models import *


@admin.register(Orders)
class Orders_admin(admin.ModelAdmin):
    list_display = ("UUID", "created",)
    list_filter = ("created",)
    search_fields = ("UUID", "adress",)