from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Cart, ProductVariation, Order, OrderItem
from products.models import InventoryProduct


# def add_to_cart(request):
#     current_user = request.user
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             product_id = int(request.POST.get('product_variation_id'))
#             quantity = int(request.POST.get('quantity'))
#             product_check = ProductVariation.objects.get(variationId=product_id)
#             if product_check:
#                 cart_item = Cart.objects.filter(user=current_user, product_id=product_id).first()
#                 if cart_item:
#                     cart_item.quantity += quantity
#                     cart_item.save()
#                 else:
#                     Cart.objects.create(user=current_user, product_id=product_id, quantity=quantity)
#                 return redirect('checkout')
#     return redirect('/')

def add_to_cart(request):
    current_user = request.user
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_variation_id'))
            quantity = int(request.POST.get('quantity'))
            try:
                product_check = ProductVariation.objects.get(variationId=product_id)
                cart_item = Cart.objects.filter(user=current_user, product_id=product_id).first()
                if cart_item:
                    cart_item.quantity += quantity
                    cart_item.save()
                else:
                    Cart.objects.create(user=current_user, product_id=product_id, quantity=quantity)
                return redirect('checkout')
            except ObjectDoesNotExist:
                pass
    return redirect('/')


def checkout(request):
    context = {}
    cart_items = Cart.objects.filter(user=request.user)

    context['cart_items'] = cart_items
    context['cart_total'] = cart_items.count()

    cart_total = 0
    total_price = 0
    if cart_items:
        for item in cart_items:
            total_price += (item.product.price) * item.quantity
            cart_total += item.quantity
        context['total_price'] = total_price
        context['cart_total'] = cart_total

    return render(request, 'profile/checkout.html', context)


class CartItemDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy('checkout')
    pk_url_kwarg = 'id'


def create_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('checkout')

    total_price = 0
    order = Order.objects.create(customer=request.user)
    for cart_item in cart_items:
        order_item = OrderItem.objects.create(order=order, product_variation=cart_item.product,
                                              quantity=cart_item.quantity,
                                              unit_price=cart_item.product.price)
        total_price += order_item.unit_price * order_item.quantity

    order.total_price = total_price
    order.save()

    cart_items.delete()

    return render(request, 'profile/order_detail.html', {'order': order})


class OrderDetailView(DetailView):
    model = Order
    template_name = 'profile/order_detail.html'
    context_object_name = 'order'
