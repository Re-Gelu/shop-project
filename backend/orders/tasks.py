from celery import shared_task
from .models import Orders
from django_celery_results.models import TaskResult
from django.utils import timezone
import datetime
from config.qiwi import get_QIWI_p2p

# Задача обработчика платежей


@shared_task
def payment_handler():
    result = ""
    p2p = get_QIWI_p2p()
    if p2p != None and (Orders.objects.filter(status=Orders.PaymentStatuses.CREATED).exists() or Orders.objects.filter(status=Orders.PaymentStatuses.WAITING).exists()):
        for order in Orders.objects.filter(status=Orders.PaymentStatuses.CREATED) or Orders.objects.filter(status=Orders.PaymentStatuses.WAITING):
            payment_status = p2p.check(order.shortuuid).status
            if order.payment_status != payment_status:
                result += f'\nOrder with id: {order.shortuuid} have new payment status {order.payment_status} -> {payment_status}. '
                order.payment_status = payment_status
                order.save()
            if payment_status == Orders.PaymentStatuses.REJECTED or payment_status == Orders.PaymentStatuses.EXPIRED:
                p2p.reject(order.shortuuid)
                result += f'Order with id: {order.shortuuid} have been deleted. '
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
    for order in Orders.objects.filter(created__lte=timezone.now() - datetime.timedelta(days=days)) and (Orders.objects.filter(status=Orders.PaymentStatuses.REJECTED) or Orders.objects.filter(status=Orders.PaymentStatuses.EXPIRED)):
        order.delete()
        count += 1
    return f"Clear done! {count} failed orders older {days} days has been deleted!"


@shared_task
def debug_task():
    print('Debug!')
