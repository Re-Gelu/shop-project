from django.contrib import admin
from .models import *


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("order_UUID", "created", "status")
    list_filter = ("created", "status")
    search_fields = ("order_UUID", "adress", "status")
