from rest_framework import serializers
from django.contrib.auth.models import User, Group
from shop.models import *
from .models import *

# Serializers


""" class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups'] """


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'id', 'name', 'price', 'promo_price', 'image',
            'information', 'full_information', 'stock',
            'available', 'created', 'updated', 'subcategory'
        ]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['id', 'name', 'category']
        
        
class DBAutoFillSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True, min_value=1, max_value=1000)
    model = serializers.CharField(required=True, min_length=1, max_length=100)
