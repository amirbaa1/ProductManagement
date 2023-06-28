from django.contrib import admin
from .models import Order, OrderItem, Cart
from accounts.models import User
from django.utils import timezone

admin.site.register(Cart)


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['customer', 'status', 'formatted_date_order']  # TODO address
    readonly_fields = ['formatted_date_order']
    list_editable = ['status']
    list_filter = ['status']

    def formatted_date_order(self, obj):
        return timezone.localtime(obj.date_order).strftime("%Y-%m-%d  %H:%M:%S")  # tehran/asia time local

    formatted_date_order.short_description = 'تاریخ و ساعت خرید'
