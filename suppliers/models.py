from django.db import models


class Supplier(models.Model):
    SupplierId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contactInfo = models.IntegerField()
