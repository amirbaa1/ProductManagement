# Generated by Django 4.2 on 2023-06-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_remove_orderitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
