import os

from celery import Celery

from django_celery_results.apps import CeleryResultConfig
from django_celery_beat.apps import BeatConfig
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', broker=settings.REDIS_URL)
      
app.config_from_object('config.settings')
app.autodiscover_tasks()

app.conf.update(result_extended=True)
app.conf.timezone = 'Europe/Moscow'

CeleryResultConfig.verbose_name = "Результаты Celery"
BeatConfig.verbose_name = "Периодические задачи"