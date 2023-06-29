from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import AboutPage, ContactUsPage, Panel_Admin, Panel_AdminOrder, View_Order, ViewInventory, \
    add_InventoryProduct, List_city_Inventory,add_cityInventory
from products.views import ProductListViews

urlpatterns = [
    # path('', ProductVariationView.as_view(), name='home'),
    path('', ProductListViews.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact_us/', ContactUsPage.as_view(), name='contact_us'),
    path('panel/', login_required(Panel_Admin.as_view()), name='panel_admin'),
    path('panel/order_customer/', Panel_AdminOrder.as_view(), name='list_order_customer'),
    path('panel/order_customer/<int:order_id>/', View_Order.as_view(), name='Det_order'),
    path('panel/inventory/', ViewInventory.as_view(), name='list_inv'),
    path('panel/add-inventory-product/', add_InventoryProduct.as_view(), name='link_add_inv_pro'),
    path('panel/list-inventory-city/', List_city_Inventory.as_view(), name='list_cit_inv'),
    path('panel/add-inventory-city/',add_cityInventory.as_view(),name = 'add_city_inv')
]
