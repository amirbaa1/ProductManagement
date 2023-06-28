from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from products.models import *


class User(AbstractUser):
    email = models.EmailField(unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('my_profile', args=[str(self.username)])


# class Authentication(AbstractUser):
#     email = models.EmailField(unique=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

#     def get_absolute_url(self):
#         return reverse('my_profile', args=[str(self.username)])
