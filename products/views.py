from django.shortcuts import render
from .models import Product, ProductVariation
from django.views.generic import ListView, DetailView


# class ProductVariationView(ListView):
#     model = ProductVariation
#     template_name = 'home.html'
#     context_object_name = 'product_v'

class ProductVariationView(ListView):
    model = ProductVariation
    template_name = 'home.html'
    context_object_name = 'product_v'

    def get_queryset(self):
        return ProductVariation.objects.filter(cityId=self.request.user.city)


class OrderCity(ListView):
    model = ProductVariation
    template_name = 'profile/checkout.html'
    context_object_name = 'order_city'

    # def get_queryset(self):
    #     return ProductVariation.objects.filter(cityId=self.request.user.city)


class ProductVariation_Detail(DetailView):
    template_name = 'details_product.html'
    model = ProductVariation
    context_object_name = 'det_pro_v'
