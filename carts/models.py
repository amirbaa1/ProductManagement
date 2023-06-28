from django.db import models
from accounts.models import User
from products.models import ProductVariation, ProductCategory
# from django_jalali.db import models as jmodels


class Order(models.Model):
    STATUS_CHOICES = (
        ('در حال بررسی سفارش', 'در حال بررسی سفارش'),
        ('در حال ارسال', 'در حال ارسال'),
        ('تحویل شده', 'تحویل شده'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام کاربر')
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ خرید')
    total_price = models.FloatField(blank=True, null=True, verbose_name='قیمت کل')
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,default='در حال بررسی سفارش')

    def __str__(self):
        return f"order {self.customer}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # date = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - Quantity: {self.quantity}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, related_name='order_items', on_delete=models.CASCADE, null=True)
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.SET_NULL, blank=True, null=True,
                                          verbose_name='نام محصول')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='انبار محصول')
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

    def __str__(self):
        return f"{self.order} - {self.product_variation} - Quantity: {self.quantity} - Unit Price: {self.unit_price}"

    def calculate_total_price(self):
        total = self.unit_price * self.quantity
        self.order.total_price = total
        self.order.save()
