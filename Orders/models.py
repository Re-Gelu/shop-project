from django.db import models
from django.utils import timezone
import datetime
from shortuuid.django_fields import ShortUUIDField

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

    product_list = models.TextField(
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

    def expire_time(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)

    def __str__(self):
        return f' Заказ №: {self.id}, UUID: {self.UUID}'

    class Meta:
        verbose_name = 'текущий заказ'
        verbose_name_plural = 'Текущие заказы'
        ordering = ('-created',)
