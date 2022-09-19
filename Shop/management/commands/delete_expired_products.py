from django.core.management.base import BaseCommand
from django.utils import timezone
from Shop.models import current_orders


class Command(BaseCommand):
    help = 'Deletes expired order rows'

    def handle(self, *args, **options):
        now = timezone.now()
        current_orders.objects.filter(expire_time__lt=now).delete()
