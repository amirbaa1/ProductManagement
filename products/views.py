from django.shortcuts import render, get_object_or_404

from carts.forms import OrderForm
from .models import Product, ProductVariation, Inventory, InventoryProduct
from django.views.generic import ListView, DetailView, TemplateView


# class ProductVariationView(ListView):
#     model = InventoryProduct
#     template_name = 'home.html'
#     context_object_name = 'product_v'

# def get_queryset(self):
#     if self.request.user.is_authenticated:
#         return InventoryProduct.objects.filter(inventoryId__cityId=self.request.user.city)
#     return InventoryProduct.objects.all()
def get_queryset(self):
    if self.request.user.is_authenticated:
        variation_id = self.request.POST.get('product_variation_id')  # دریافت variationId از درخواست POST
        if variation_id:
            variation = get_object_or_404(ProductVariation, variationId=variation_id)
            return InventoryProduct.objects.filter(inventoryId__cityId=self.request.user.city,
                                                   productId=variation.productId)
        else:
            return InventoryProduct.objects.filter(inventoryId__cityId=self.request.user.city)
    return InventoryProduct.objects.all()


# def get_queryset(self): # حذف تکراری
#     queryset = super().get_queryset()
#     products_dict = {}
#     for product in queryset:
#         if product.productId.name not in products_dict:
#             products_dict[product.productId.name] = product
#     queryset = list(products_dict.values())
#     return queryset


# class InventoryView(ListView):
#     model = InventoryProduct
#     template_name = 'details_product.html'
#     context_object_name = 'product_Invent'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product = self.get_object()  # فرضاً محصول مورد نظر
#         inventories = InventoryProduct.objects.filter(productId=product.productId)
#         context['product_Invent'] = inventories
#         return context


class OrderCity(ListView):
    model = Inventory
    template_name = 'profile/checkout.html'
    context_object_name = 'order_city'

    def get_queryset(self):
        return Inventory.objects.filter(cityId=self.request.user.city)


class ProductVariation_Detail(DetailView):
    template_name = 'details_product.html'
    model = InventoryProduct
    context_object_name = 'det_pro_v'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_variation = self.get_object().productId  # محصول مورد نظر

        inventories = InventoryProduct.objects.filter(productId=product_variation)
        context['product_Invent'] = inventories

        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     product = self.get_object()  # فرضاً محصول مورد نظر
    #     inventories = InventoryProduct.objects.filter(productId=product.productId)
    #     context['product_Invent'] = inventories
    #     return context


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     product = self.get_object().productId  # فرضاً محصول مورد نظر
#
#     # استخراج مقدار product_variation_id از روی URL
#     product_variation_id = self.kwargs.get('pk')
#
#     # استخراج مدل ProductVariation بر اساس product_variation_id
#     product_variation = get_object_or_404(ProductVariation, pk=product_variation_id)
#
#     inventories = InventoryProduct.objects.filter(productId=product)
#     context['product_Invent'] = inventories
#
#     # ایجاد نمونه از فرم OrderForm و ارسال product_variation به آن
#     order_form = OrderForm(product_variation=product_variation)
#     context['order_form'] = order_form
#     return context


# class categoryPage(ListView):
#     model = ProductVariation
#     template_name = 'category.html'
#     context_object_name = 'cot'

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['product_v'] = InventoryProduct.objects.all()
        return context
