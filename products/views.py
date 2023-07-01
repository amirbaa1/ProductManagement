from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from .forms import Form_add_product
from .models import ProductCategory, ProductVariation, InventoryProduct, City
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.admin.views.decorators import user_passes_test


# class ProductVariationView(ListView):
#     model = ProductVariation
#     template_name = 'home.html'
#     context_object_name = 'product_v'

class ProductListViews(View):
    def get(self, request):
        product_v = ProductVariation.objects.all()
        product_list = ProductCategory.objects.all()
        default_product_v = ProductVariation.objects.all()

        category = request.GET.get('categories')
        # category_city = request.GET.get('categories_city')

        # if category:
        #     product_v = ProductVariation.objects.filter(productId=category)
        # product_v = ProductVariation.objects.filter(Q(productId=category) & Q(cityId=category_city))

        # if category_city:
        #     product_v = product_v.filter(cityId=category)

        if category:
            product_v = product_v.filter(productId=category)
            messages.success(request, 'مکان موقعیت شما خارج از انبار محلی شما است.')

        elif request.user.is_authenticated:
            product_v = product_v.filter(cityId=request.user.city)
            messages.success(request, f' موقعیت محلی  : {self.request.user.city} هستید ')
        else:
            product_v = default_product_v
            messages.success(request, 'کل محصولات')
        context = {
            'product_v': product_v,
            'cat': product_list,
        }
        return render(request, 'home.html', context=context)


class ProductVariation_Detail(DetailView):
    template_name = 'details_product.html'
    model = ProductVariation
    context_object_name = 'det_pro_v'


class CreateProduct(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'products.add_productvariation'
    model = ProductVariation
    template_name = 'admin/add_product.html'
    form_class = Form_add_product
    context_object_name = 'create_prov'

    def get_success_message(self, cleaned_data):
        return f"محصول {self.object.name} اضافه شد."

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)
