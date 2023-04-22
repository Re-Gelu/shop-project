from rest_framework import serializers
from .models import Orders

# Serializers


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            'id', 'user_id', 'order_UUID', 'order_info',
            'cart', 'adress', 'contacts', 'created', 'updated',
            'payment_link', 'status'
        ]
