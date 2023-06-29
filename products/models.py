from django.db import models
from django.urls import reverse, reverse_lazy


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


class ProductCategory(models.Model):
    productId = models.AutoField(primary_key=True)  # create primary ky by AutoFild
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        # return reverse('pro_v', args=[str(self.pk)])
        return reverse_lazy('link_list_pro_v')
class ProductVariation(models.Model):
    variationId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='دسته محصول')
    name = models.CharField(max_length=30, verbose_name='نام محصول')
    Supplier = models.ManyToManyField('Supplier')
    price = models.IntegerField(verbose_name='قیمت (تومان)', help_text='یک بسته 500 گرمی')
    quantity = models.IntegerField(verbose_name='تعداد کالا')
    cityId = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='انبار', null=True)
    text = models.TextField(max_length=1000, null=True, blank=True, help_text='اجبار پر کردن توضیحات نیست',
                            verbose_name='توضیح محصول')

    def get_absolute_url(self):
        # return reverse('pro_v', args=[str(self.pk)])
        return reverse_lazy('link_list_pro_v')

    def __str__(self):
        return f"{self.name} {self.Supplier.first()}"


class Inventory(models.Model):
    inventoryId = models.AutoField(primary_key=True)
    cityId = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cityId}"

    def get_absolute_url(self):
        return reverse_lazy('list_cit_inv')


class InventoryProduct(models.Model):
    inventoryProductId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='تعداد کالا')
    inventoryId = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.inventoryId}--{self.productId}"

    def get_absolute_url(self):
        return reverse_lazy('list_inv')


class Supplier(models.Model):
    SupplierId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text='نام برند یا تامین کنندگان', verbose_name='نام تامین کنندگان')
    contactInfo = models.IntegerField(verbose_name='شماره تلفن')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy('link_sup_list')
