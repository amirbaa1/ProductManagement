from django.urls import path
from .views import *

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name="checkout"),
    path('delete-cart/<int:id>/', CartItemDeleteView.as_view(), name='delete-cart'),
    path('create-order/', create_order, name='order_create'),
    path('order-detail/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
