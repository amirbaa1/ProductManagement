from django.contrib import admin
from .models import Order, OrderItem, Cart
from accounts.models import User

admin.site.register(Cart)


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['customer']
