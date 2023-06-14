from django.contrib import admin
from .models import Product, ProductVariation, InventoryProduct, Inventory, City


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    list_filter = ['name']


@admin.register(ProductVariation)
class AdminProductVariation(admin.ModelAdmin):
    list_display = ['productId', 'name', 'price', 'quantity']
    list_filter = ['productId']


@admin.register(Inventory)
class AdminInventory(admin.ModelAdmin):
    list_display = ['cityId']


@admin.register(InventoryProduct)
class AdminInventoryProduct(admin.ModelAdmin):
    list_display = ['inventoryId', 'productId','status']
    list_filter = ['inventoryId', 'productId','status']
    list_editable = ['status']


@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ['name']
