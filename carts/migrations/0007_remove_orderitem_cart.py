# Generated by Django 4.2 on 2023-06-16 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart',
        ),
    ]
