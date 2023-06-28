from django.contrib import admin
from .models import ProductCategory, ProductVariation, InventoryProduct, Inventory, City, Supplier


@admin.register(ProductCategory)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(ProductVariation)
class AdminProductVariation(admin.ModelAdmin):
    # list_display = ['productId', 'name', 'Supplier', 'price', 'quantity', 'cityId']
    list_display = ['productId', 'name', 'get_supplier_names', 'price', 'quantity', 'cityId']
    list_filter = ['productId', 'Supplier', 'cityId']

    def get_supplier_names(self, obj):
        return ", ".join([supplier.name for supplier in obj.Supplier.all()])
    get_supplier_names.short_description = 'Suppliers'


@admin.register(Inventory)
class AdminInventory(admin.ModelAdmin):
    list_display = ['cityId']


@admin.register(InventoryProduct)
class AdminInventoryProduct(admin.ModelAdmin):
    list_display = ['inventoryId', 'productId', 'quantity']


@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contactInfo']
