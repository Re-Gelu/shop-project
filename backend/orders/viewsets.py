from cart.cart import Cart
from config.qiwi import get_QIWI_p2p
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from extra_settings.models import Setting
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from shop.models import *

from .forms import *
from .models import *
from .serializers import *

# Кэшируются только GET и HEAD ответы со статусом 200
default_decorators = (cache_page(getattr(settings, 'CACHING_TIME', 60)), vary_on_headers("Authorization",))


# ViewSets

@method_decorator(default_decorators, name="dispatch")
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = {
        'shortuuid': ['exact', 'contains', ],
        'created': ['gte', 'lte'],
        'user_id': ['exact',]
    }

    def create(self, request):
        cart = Cart(request)
        p2p = get_QIWI_p2p()

        # Если ключа QIWI нет или он не прошел проверку
        if p2p == None:
            return Response({"error": "Set QIWI_PRIVATE_KEY setting!"}, status=status.HTTP_400_BAD_REQUEST)

        # Add and update data to save in bd
        request.data.update({"cart": list(cart)})
        request.data.update({"user_id": request.user.id})
        request.data.update({"order_info": ""})
        for key, item in enumerate(cart):
            request.data["order_info"] += f"\n{key + 1}) ID товара: {item.get('id')}, Наименование товара: {item.get('name')}"
            request.data["order_info"] += f", Общая стоимость товара: {item.get('total_promo_price')}$" if 'total_promo_price' in item else f", Общая стоимость товара: {item.get('total_price')}$"

        request.data["order_info"] += f"\n\nИТОГО: {cart.get_total_promo_price()} RUB"

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        headers = self.get_success_headers(serializer.data)

        # Создание QIWI платежа
        site_name = Setting.get("SITE_NAME")
        bill = p2p.bill(
            bill_id=order.shortuuid,
            amount=cart.get_total_promo_price(),
            lifetime=Setting.get("QIWI_PAYMENTS_LIFETIME"),
            comment=f"{site_name} - Заказ №{order.shortuuid}"
        )
        
        success_payment_url = getattr(settings, "SUCCESS_PAYMENT_URL", "")

        # Доабавление ссылки на оплату
        order.payment_link = bill.pay_url + \
            f"&successUrl={success_payment_url}"
        order.save()
        serializer = self.get_serializer(order)

        # Очищаем корзину
        cart.clear()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
