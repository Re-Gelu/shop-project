from django.contrib import admin
from .models import *


@admin.register(orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("UUID", "created", "status")
    list_filter = ("created", "status")
    search_fields = ("UUID", "adress", "status")
