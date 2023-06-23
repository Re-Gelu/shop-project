from rest_framework import serializers
from .models import Orders

# Serializers


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        read_only_fields = ('shortuuid', 'cart',
                            'user_id', 'payment_status', 'payment_link')
