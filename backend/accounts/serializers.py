from django.contrib.auth.models import Group, User
from djoser import serializers as djoser_serializers
from djoser.conf import settings
from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework import serializers


class CustomUserSerializer(djoser_serializers.UserSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        additional_fields = (
            'groups', 'is_staff',
            'is_superuser', 'is_active',
            'first_name', 'last_name',
            'orders',
        )
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        ) + additional_fields
        read_only_fields = (settings.LOGIN_FIELD, ) + additional_fields

    def get_orders(self, obj):
        queryset = Orders.objects.filter(
            user_id=obj.id
        ).order_by('-id')
        serializer = OrdersSerializer(queryset, many=True)
        return serializer.data


class CustomUserCreateSerializer(djoser_serializers.UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        ) + (
            'first_name', 'last_name'
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
