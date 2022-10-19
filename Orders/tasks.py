from celery import shared_task
from django.conf import settings
from extra_settings.models import Setting
from pyqiwip2p import QiwiP2P
from .models import Orders

# QIWI payments
p2p = QiwiP2P(auth_key=settings.QIWI_PRIVATE_KEY if Setting.get("QIWI_PRIVATE_KEY") == "" else Setting.get("QIWI_PRIVATE_KEY"))

@shared_task
def payment_handler():
    result = "Waiting for new payment statuses..."
    for order in Orders.objects.filter(status=Orders.Payment_statuses.CREATED) or Orders.objects.filter(status=Orders.Payment_statuses.WAITING):
        payment_status = p2p.check(order.UUID).status
        if order.status != payment_status:
            result = f'Order with id: {order.UUID} have new payment status {order.status} -> {payment_status}'
            order.status = payment_status
            order.save()
        if payment_status == Orders.Payment_statuses.REJECTED or payment_status == Orders.Payment_statuses.EXPIRED:
            result1 = f'\nOrder with id: {order.UUID} have been deleted!'
            p2p.reject(order.UUID)
            return result + result1
        return result
    return result
            
@shared_task
def debug_task():
    print('Debug!')