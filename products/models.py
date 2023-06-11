from django.db import models
from django.urls import reverse


class City(models.Model):
    TYPE_CHOICES = (
        ("آبادان", "آبادان"),
        ("بوشهر", "بوشهر"),
        ("تهران", "تهران"),
        ("کرج", "کرج"),
        ("تبریز", "تبریز"),
        ("مشهد", "مشهد"),
        ("اصفهان", "اصفهان"),
        ("شیراز", "شیراز"),
        ("قم", "قم"),
        ("قشم", "قشم"),
        ("کرمان", "کرمان"),
        ("کردستان", "کردستان"),
    )
    name = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    productId = models.AutoField(primary_key=True)  # create primary ky by AutoFild
    name = models.CharField(max_length=30, verbose_name="نام")
    price = models.IntegerField(verbose_name="قیمت")
    quantity = models.IntegerField(verbose_name="تعداد")
    # type = models.CharField(max_length=30, verbose_name="نوع محصول")
    cityId = models.ForeignKey(City, on_delete=models.CASCADE, null=True, verbose_name="شهر")

    def __str__(self):
        return f"{self.name}"


class ProductVariation(models.Model):
    variationId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='نام دسته بندی')
    name = models.CharField(max_length=30, verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')
    quantity = models.IntegerField(verbose_name='تعداد')
    text = models.TextField(max_length=2000, null=True, blank=True, verbose_name='توضیح کالا')
    cityId = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='شهر')

    def get_absolute_url(self):
        return reverse('pro_v', args=[str(self.pk)])

    def __str__(self):
        return f"{self.name}"


class Inventory(models.Model):
    inventoryId = models.AutoField(primary_key=True)
    cityId = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cityId}"


class InventoryProduct(models.Model):
    inventoryProductId = models.AutoField(primary_key=True)
    inventoryId = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    productId = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.inventoryId}  {self.productId} {self.quantity}"
