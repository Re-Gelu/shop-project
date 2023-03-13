# Generated by Django 4.0.8 on 2023-03-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orders_cart_alter_orders_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product_list',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_info',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='Список товаров'),
        ),
    ]