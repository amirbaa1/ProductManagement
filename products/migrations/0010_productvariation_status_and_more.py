# Generated by Django 4.2 on 2023-06-11 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_cityid_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='cityId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='name',
            field=models.CharField(max_length=30, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variations', to='products.product', verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='quantity',
            field=models.IntegerField(verbose_name='تعداد'),
        ),
    ]