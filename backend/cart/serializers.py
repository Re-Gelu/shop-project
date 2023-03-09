from rest_framework import serializers

# Serializers


class CartSerializer(serializers.ListSerializer):
    child = serializers.DictField()


class CartActionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, min_value=1)
    action = serializers.BooleanField(default=True)
    amount = serializers.IntegerField(min_value=1, max_value=100, default=1)
