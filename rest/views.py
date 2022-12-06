from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import generics 
from Cart.cart import Cart
from .serializers import *
from Shop.models import *
from Orders.models import *
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from Shop.models import Products


class CartViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = [item for item in Cart(request)]
        serializer = CartSerializer(queryset)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CartActionSerializer(data=request.data)
        if serializer.is_valid():
            product = get_object_or_404(
                Products, id=serializer.validated_data.get("id"))
            action = serializer.validated_data.get("action")
            amount = serializer.validated_data.get("amount")
            Cart(request).action(
                product=product,
                action=action,
                amount=amount
            )
            return Response(Cart(request).get_cart_list(), status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        Cart(request).clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['post'])
    def cart_action(self, request):
        serializer = CartActionSerializer(data=request.data)
        if serializer.is_valid():
            product = get_object_or_404(Products, id=serializer.validated_data.get("id"))
            action = serializer.validated_data.get("action")
            amount = serializer.validated_data.get("amount")
            Cart(request).action(
                product=product, 
                action=action,
                amount=amount
            )
            return Response(Cart(request).get_cart_list(), status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartAPIView(APIView):
    
    def get(self, request, format=None):
        return Response(Cart(request).get_cart_list())
    
    def post(self, request, format=None):
        if request.data:
            product = get_object_or_404(Products, id=request.data.get("id"))
            action = request.data.get("action")
            Cart(request).action(product=product, action=action)
            return Response(Cart(request).get_cart_list(), status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        Cart(request).clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ViewSets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
        
        
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SubcategoriesViewSet(viewsets.ModelViewSet):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
