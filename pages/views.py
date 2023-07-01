from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from carts.forms import Status_Update
from products.forms import Form_add_cityInventory, Form_add_Inventory_product, Form_Update_Supplier, Form_Update_ProV, \
    Form_add_Supplier, Form_add_category_product
from products.models import Supplier, InventoryProduct, Inventory, ProductVariation, ProductCategory, City
from carts.models import OrderItem, Order
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class AboutPage(ListView):
    model = Supplier
    template_name = 'about.html'
    context_object_name = 'supp'


class ContactUsPage(TemplateView):
    template_name = 'contact_us.html'


class Panel_Admin(TemplateView):
    template_name = 'admin/panel.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


# class Panel_AdminOrder(ListView):
#     model = Order
#     template_name = 'admin/Order.html'
#     context_object_name = 'admin_order'
#     ordering = ['-id']
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_superuser:
#             return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
#         return super().dispatch(request, *args, **kwargs)


# def staff_required(login_url=None):
#     return user_passes_test(lambda u: u.is_staff, login_url=login_url)
#

class Panel_AdminOrder(View):
    @method_decorator(permission_required('carts.view_order'))
    def get(self, request):
        order_list = Order.objects.order_by('-date_order')
        order_cat_status = [
            ('در حال بررسی سفارش', 'در حال بررسی سفارش'),
            ('در حال ارسال', 'در حال ارسال'),
            ('تحویل شده', 'تحویل شده'),
        ]
        category_status = request.GET.get('cat_status')

        if category_status:
            order_list = order_list.filter(status=category_status)

        context = {
            'category_status': order_cat_status,
            'admin_order': order_list
        }

        return render(request, 'admin/Order.html', context=context)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


# class Detail_Order(DetailView):
#     model = Order
#     template_name = 'admin/order_customer.html'
#     context_object_name = 'order'
#
#
# class Update_OrderItem(UpdateView):
#     model = Order
#     fields = ['status']
#     template_name = 'admin/update_status.html'
#     context_object_name = 'order_item'
#     success_url = '/panel/order_customer/'


class View_Order(View):
    @method_decorator(permission_required('carts.view_orderitem'))
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        order_items = OrderItem.objects.filter(order=order)

        context = {'order': order,
                   'order_items': order_items,
                   }

        return render(request, 'admin/order_customer.html', context=context)

    def post(self, request, order_id, *args, **kwargs):
        order = Order.objects.get(pk=order_id)
        status_form = Status_Update(request.POST, instance=order)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'سفارش با موفقیت تغییر کرد.')

        return render(request, 'admin/order_customer.html', {'order': order, 'status_form': status_form})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class ViewInventory(ListView):
    model = InventoryProduct
    template_name = 'admin/Inventory.html'
    context_object_name = 'inv_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Delete_Inventory(SuccessMessageMixin, DeleteView):
    model = InventoryProduct
    success_url = reverse_lazy('list_inv')
    pk_url_kwarg = 'id'

    def get_success_message(self, cleaned_data):
        return f'انبار {self.object.inventoryId} و محصول {self.object.productId} حذف شد .'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class add_InventoryProduct(SuccessMessageMixin, CreateView):
    model = InventoryProduct
    template_name = 'admin/add_InventoryPro.html'
    # fields = '__all__'
    form_class = Form_add_Inventory_product
    context_object_name = 'add_inv_pro'

    def get_success_message(self, cleaned_data):
        return f'محصول {self.object.productId} در انبار {self.object.inventoryId} اضافه شد. '

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class List_city_Inventory(ListView):
    model = Inventory
    template_name = 'admin/list_inventory.html'
    context_object_name = 'list_invcity'
    ordering = ['-inventoryId']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class add_cityInventory(SuccessMessageMixin, CreateView):
    model = Inventory
    template_name = 'admin/add_city_inventory.html'
    # fields = '__all__'
    form_class = Form_add_cityInventory
    context_object_name = 'add_city_inv'

    # success_message = 'انبار اضافه شد.'

    def get_success_message(self, cleaned_data):
        return f'انبار {self.object.cityId} اضافه شد.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Delete_city_inventory(SuccessMessageMixin, DeleteView):
    model = Inventory
    success_url = reverse_lazy('list_cit_inv')
    pk_url_kwarg = 'id'

    def get_success_message(self, cleaned_data):
        return f'انبار {self.object.cityId} حذف شد.'


class List_Supplier(ListView):
    model = Supplier
    template_name = "admin/supplier.html"
    context_object_name = 'sup_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Delete_Supplier(SuccessMessageMixin, DeleteView):
    model = Supplier
    success_url = reverse_lazy('link_sup_list')
    pk_url_kwarg = 'id'

    def get_success_message(self, cleaned_data):
        return f"تامین کننده {self.object.name} حذف شد."

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class add_Supplier(SuccessMessageMixin, CreateView):
    model = Supplier
    template_name = 'admin/add_supplier.html'
    # fields = '__all__'
    form_class = Form_add_Supplier
    context_object_name = 'add_spp'

    def get_success_message(self, cleaned_data):
        return f'نام تامین کننده {self.object.name} اضافه شد.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Update_Supplier(SuccessMessageMixin, UpdateView):
    model = Supplier
    template_name = 'admin/update_supplier.html'
    form_class = Form_Update_Supplier
    # fields = '__all__'
    pk_url_kwarg = 'id'

    def get_success_message(self, cleaned_data):
        return 'با موفقیت اپدیت شد.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


# class Product_vari_List(ListView):
#     model = ProductVariation
#     template_name = 'admin/product_variation.html'
#     context_object_name = 'pro_lit'
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_superuser:
#             return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
#         return super().dispatch(request, *args, **kwargs)

# @permission_required('products.view_product_variation')
class Product_view_list(View):
    @method_decorator(permission_required('products.view_productvariation'))
    def get(self, request):
        product_v_list = ProductVariation.objects.all()
        product_cat_admin = ProductCategory.objects.all()
        city = City.objects.all()

        category = request.GET.get('categories_admin')
        category_city = request.GET.get('categories_city_admin')

        if category:
            product_v_list = product_v_list.filter(productId=category)

        if category_city:
            product_v_list = product_v_list.filter(cityId=category_city)

        if category_city and category:
            product_v_list = product_v_list.filter(cityId=category_city, productId=category)

        context = {
            'pro_list': product_v_list,
            'cat1': product_cat_admin,
            'cat_city': city,
        }
        return render(request, 'admin/product_variation.html', context=context)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Update_Pro_v(PermissionRequiredMixin, UpdateView):
    permission_required = 'products.change_productvariation'
    model = ProductVariation
    template_name = 'admin/update_pro_va.html'
    pk_url_kwarg = 'id'
    form_class = Form_Update_ProV

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Delete_ProductVariation(SuccessMessageMixin, DeleteView):
    model = ProductVariation
    success_url = reverse_lazy('link_list_pro_v')
    pk_url_kwarg = 'id'

    def get_success_message(self, cleaned_data):
        return f"محصول {self.object.name} حذف شد."


class add_category_product(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'products.add_productcategory'
    model = ProductCategory
    template_name = 'admin/add_product_category.html'
    # fields = '__all__'
    form_class = Form_add_category_product
    context_object_name = 'add_spp'

    def get_success_message(self, cleaned_data):
        return f'نام دسته جدید {self.object.name} اضافه شد.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class List_cat_product(PermissionRequiredMixin, ListView):
    permission_required = 'products.view_productcategory'
    model = ProductCategory
    template_name = 'admin/list_product_cat.html'
    context_object_name = 'list_cat_pro'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Delete_cat_pro(PermissionRequiredMixin, DeleteView):
    permission_required = 'products.delete_productcategory'
    model = ProductCategory
    success_url = reverse_lazy('link_list_pro_cat')
    pk_url_kwarg = 'id'

    def get_success_message(self, cleaned_data):
        return f"دسته بندی {self.object.name} حذف شد."




