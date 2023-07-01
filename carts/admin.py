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
    list_display = ['customer','order_items__city','status', 'formatted_date_order']
    readonly_fields = ['formatted_date_order']
    list_editable = ['status']
    list_filter = ['status']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('order_items')
        return queryset

    def order_items__city(self, obj):
        return obj.order_items.first().city if obj.order_items.exists() else None

    order_items__city.short_description = 'شهر کاربر'

    def formatted_date_order(self, obj):
        return timezone.localtime(obj.date_order).strftime("%Y-%m-%d  %H:%M:%S")  # tehran/asia time local

    formatted_date_order.short_description = 'تاریخ و ساعت خرید'
