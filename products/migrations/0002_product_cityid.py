# Generated by Django 4.2 on 2023-06-02 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cityId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.city'),
        ),
    ]
