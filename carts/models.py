from django.db import models
from accounts.models import User
from products.models import ProductVariation, Product, City


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"order {self.customer}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - Quantity: {self.quantity}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='order_items', on_delete=models.CASCADE, null=True)
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='شهر')
    status = models.CharField(max_length=50,choices=(('در حال ارسال', 'در حال ارسال'), ('در حال بررسی سفارش', 'درحال بررسی سفارش')),
                              default='درحال بررسی سفارش', verbose_name='وضعیت سفارش')

    def __str__(self):
        return f"{self.order} - {self.product_variation} - Quantity: {self.quantity} - Unit Price: {self.unit_price}"

    def calculate_total_price(self):
        total = self.unit_price * self.quantity
        self.order.total_price = total
        self.order.save()
