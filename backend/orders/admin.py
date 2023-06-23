from django.contrib import admin
from .models import *


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("shortuuid", "created", "payment_status")
    list_filter = ("created", "payment_status")
    search_fields = ("shortuuid", "adress", "payment_status")
