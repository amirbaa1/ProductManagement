from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class AdminSupplier(admin.ModelAdmin):
    list_display = ['name', 'contactInfo']
