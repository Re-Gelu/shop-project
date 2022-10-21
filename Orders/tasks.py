from celery import shared_task
from .models import Orders
from django_celery_results.models import TaskResult
from django.utils import timezone
import datetime
from .QIWI import get_QIWI_p2p

@shared_task
def payment_handler():
    result = "Waiting for new payment statuses..."
    p2p = get_QIWI_p2p()
    if p2p != False and (Orders.objects.filter(status=Orders.Payment_statuses.CREATED).exists() or Orders.objects.filter(status=Orders.Payment_statuses.WAITING).exists()):
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
    else:
        return "No orders to handle for now..."
    
def delete_1_week_old_payment_handler_results():
    for order in TaskResult.objects.filter(date_done__lte=timezone.now() - datetime.timedelta(days=7)):
        #order.delete()
        pass
            
@shared_task
def debug_task():
    print('Debug!')