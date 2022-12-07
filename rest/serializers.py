from rest_framework import serializers
from django.contrib.auth.models import User, Group
from Shop.models import *
from Orders.models import *

# Serializers

class CartSerializer(serializers.ListSerializer):
    child = serializers.DictField()
    

class CartActionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, min_value=1)
    action = serializers.BooleanField(default=True)
    amount = serializers.IntegerField(min_value=1, max_value=100, default=1)
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        

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
        

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            'id', 'user_id', 'UUID', 'product_info',
            'adress', 'contacts', 'created', 'updated', 
            'status', 'cart'
        ]
