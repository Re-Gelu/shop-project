from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from shop.models import Products
from .serializers import *
from .cart import Cart
import django.contrib.auth

# ViewSets


class CartViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        cart = Cart(request)
        queryset = [item for item in cart]
        serializer = CartSerializer(queryset)
        response = {
            "cart": serializer.data,
            "cart_total_price": cart.get_total_price(),
            "cart_total_promo_price": cart.get_total_promo_price(),
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Id of the product', default=1),
                'action': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='True - add to cart, False - remove from cart', default=True),
                'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='Amount of the product', default=1),
            }
        ),
        responses={'201': CartActionSerializer}
    )
    def create(self, request):
        cart = Cart(request)
        serializer = CartActionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        cart.action(
            product=get_object_or_404(
                Products,
                id=serializer.validated_data.get("id")
            ),
            action=serializer.validated_data.get("action"),
            amount=serializer.validated_data.get("amount")
        )
        
        response = {
            "cart": cart.get_cart_list(),
            "cart_total_price": cart.get_total_price(),
            "cart_total_promo_price": cart.get_total_promo_price(),
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        product = get_object_or_404(
            Products,
            id=int(pk)
        )
        Cart(request).remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(operation_description="GET /cart/{id}/")
    def retrieve(self, request, pk=None):
        cart = list(Cart(request))
        if 0 <= int(pk) < len(cart):
            return Response(cart[int(pk)], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def clear(self, request):
        Cart(request).clear()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
