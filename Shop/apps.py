from django.apps import AppConfig
from watson import search as watson

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Shop'
    verbose_name = 'Магазин'

    def ready(self):
        watson.register(self.get_model("Products"))
