# Generated by Django 4.2 on 2023-06-29 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productcategory_remove_inventoryproduct_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='cityId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.city', verbose_name='انبار'),
        ),
    ]