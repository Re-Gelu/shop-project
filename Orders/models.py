from django.db import models
from django.utils import timezone
from typing import Iterable
from shortuuid.django_fields import ShortUUIDField
from payments import PurchasedItem
from payments.models import BasePayment
from decimal import Decimal
import datetime
class Orders(models.Model):
    
    user_id = models.PositiveIntegerField(
        editable=False,
    )

    UUID = ShortUUIDField(
        auto_created=True, 
        alphabet="0123456789",
        unique=True,
        verbose_name="UUID заказа",
        length=10,
        max_length=10,
        editable=False,
    )

    product_info = models.TextField(
        blank=True, null=True,
        verbose_name="Список товаров",
    )

    adress = models.TextField(
        blank=True, null=True,
        verbose_name="Адрес клиента",
    )

    contacts = models.TextField(
        blank=True, null=True,
        verbose_name="Контакты клиента",
    )

    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания заказа"
    )
    
    order_cart = models.JSONField(
        editable=False,
    )

    def expire_time(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)

    def __str__(self):
        return f' Заказ №: {self.id}, UUID: {self.UUID}'

    class Meta:
        verbose_name = 'текущий заказ'
        verbose_name_plural = 'Текущие заказы'
        ordering = ('-created',)
        

""" class Payment(BasePayment):
    
    order_UUID = ShortUUIDField()

    # Return a URL where users are redirected after they fail to complete a payment:
    def get_failure_url(self) -> str:
        return f"payments/{self.pk}/failure"

    # Return a URL where users are redirected after they successfully complete a payment:
    def get_success_url(self) -> str:
        return f"payments/{self.pk}/success"

    # Return items that will be included in this payment.
    def get_purchased_items(self) -> Iterable[PurchasedItem]:
        order = Orders.objects.get(UUID=self.order_UUID)
        if order:
            for item in order.order_cart.values():
                yield PurchasedItem(
                    name=item['name'],
                    sku='BSKV',
                    quantity=item['product_amount'],
                    price=Decimal(item['total_price']),
                    currency='USD',
                ) """
