from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from .serializers import *
from Shop.models import *
from Orders.models import *
from Shop.models import Products
from Cart.cart import Cart

# ViewSets

class CartViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    
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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
        
        
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


class HeaderOffcanvasBodyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart_offcanvas_body.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            "cart": Cart(request)
        }
        return Response(context)


class DashboardCartView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard_cart.html'

    def get(self, request, *args, **kwargs):
        context = {
            "cart": Cart(request)
        }
        return Response(context)
