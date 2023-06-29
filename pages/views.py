from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from carts.forms import Status_Update
from products.models import Supplier, InventoryProduct, Inventory
from carts.models import OrderItem, Order
from django.contrib import messages


class AboutPage(ListView):
    model = Supplier
    template_name = 'about.html'
    context_object_name = 'supp'


class ContactUsPage(TemplateView):
    template_name = 'contact_us.html'


class Panel_Admin(TemplateView):
    template_name = 'admin/panel.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


class Panel_AdminOrder(ListView):
    model = Order
    template_name = 'admin/Order.html'
    context_object_name = 'admin_order'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("<b><h2>دسترسی ممنوع است</h2></b><h4> .فقط مدیر سایت میتواند وارد شود</h4>")
        return super().dispatch(request, *args, **kwargs)


# class Detail_Order(DetailView):
#     model = Order
#     template_name = 'admin/order_costumer.html'
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
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        order_items = OrderItem.objects.filter(order=order)

        return render(request, 'admin/order_costumer.html', {'order': order, 'order_items': order_items,
                                                             })

    def post(self, request, order_id, *args, **kwargs):
        order = Order.objects.get(pk=order_id)
        status_form = Status_Update(request.POST, instance=order)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'سفارش با موفقیت تغییر کرد.')

        return render(request, 'admin/order_costumer.html', {'order': order, 'status_form': status_form})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
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


class add_InventoryProduct(CreateView):
    model = InventoryProduct
    template_name = 'admin/add_InventoryPro.html'
    fields = '__all__'
    context_object_name = 'add_inv_pro'


class List_city_Inventory(ListView):
    model = Inventory
    template_name = 'admin/list_inventory.html'
    context_object_name = 'list_inv_city'


class add_cityInventory(CreateView):  # TODO fix error ImproperlyConfigured
    model = Inventory
    template_name = 'admin/add_city_inventory.html'
    fields = '__all__'
    context_object_name = 'add_city_inv'
