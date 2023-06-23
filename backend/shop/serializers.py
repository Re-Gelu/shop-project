from rest_framework import serializers
from shop.models import *

from .models import *

# Serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'id', 'name', 'price', 'promo_price', 'image',
            'information', 'full_information', 'stock',
            'available', 'created', 'updated', 'subcategory',
            'category', 'was_publiched_recently'
        ]


class ProductsWithAbsoluteURLSerializer(ProductsSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request is not None:
            data['image'] = request.build_absolute_uri(data['image'])
        return data


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
    
    
class IndexPageItemSerializer(serializers.ModelSerializer):
    products = serializers.ListField()
    subcategories = SubcategoriesSerializer(many=True)
    
    class Meta:
        model = Categories
        fields = ['id', 'name', 'subcategories', 'products']
        

class IndexPageSerializer(serializers.ListSerializer):
    child = IndexPageItemSerializer()