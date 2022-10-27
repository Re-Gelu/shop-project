from celery import shared_task
from .models import Orders
from django_celery_results.models import TaskResult
from django.utils import timezone
from celery.result import AsyncResult
import datetime
from .QIWI import get_QIWI_p2p

# Задача обработчика платежей
@shared_task
def payment_handler():
    result = ""
    p2p = get_QIWI_p2p()
    if p2p != False and (Orders.objects.filter(status=Orders.Payment_statuses.CREATED).exists() or Orders.objects.filter(status=Orders.Payment_statuses.WAITING).exists()):
        for order in Orders.objects.filter(status=Orders.Payment_statuses.CREATED) or Orders.objects.filter(status=Orders.Payment_statuses.WAITING):
            payment_status = p2p.check(order.UUID).status
            if order.status != payment_status:
                result += f'\nOrder with id: {order.UUID} have new payment status {order.status} -> {payment_status}. '
                order.status = payment_status
                order.save()
            if payment_status == Orders.Payment_statuses.REJECTED or payment_status == Orders.Payment_statuses.EXPIRED:
                p2p.reject(order.UUID)
                result += f'Order with id: {order.UUID} have been deleted. '
        return result if result != "" else "Waiting for new payment statuses..."
    else:
        return "No orders to handle for now..."

# Задача для удаления ВСЕХ старых результатов платежей
@shared_task
def delete_old_payment_handler_results(days=7):
    count = 0
    for result in TaskResult.objects.filter(date_done__lte=timezone.now() - datetime.timedelta(days=days)):
        result.delete()
        count += 1
    return f"Clear done! {count} results older {days} days has been deleted!"

# Задача для удаления всех заказов старше N дней
@shared_task
def delete_all_old_orders(days=7):
    count = 0
    for order in Orders.objects.filter(created__lte=timezone.now() - datetime.timedelta(days=days)):
        order.delete()
        count += 1
    return f"Clear done! {count} orders older {days} days has been deleted!"

# Задача для удаления всех неудавшихся заказов старше N дней
@shared_task
def delete_all_failed_old_orders(days=7):
    count = 0
    for order in Orders.objects.filter(created__lte=timezone.now() - datetime.timedelta(days=days)) and (Orders.objects.filter(status=Orders.Payment_statuses.REJECTED) or Orders.objects.filter(status=Orders.Payment_statuses.EXPIRED)):
        order.delete()
        count += 1
    return f"Clear done! {count} failed orders older {days} days has been deleted!"


@shared_task
def debug_task():
    print('Debug!')
