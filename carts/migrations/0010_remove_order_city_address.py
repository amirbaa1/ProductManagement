# Generated by Django 4.2 on 2023-06-22 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_order_city_address_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city_address',
        ),
    ]
