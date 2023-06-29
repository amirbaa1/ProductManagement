from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
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
    path('panel/add-inventory-city/', add_cityInventory.as_view(), name='add_city_inv'),
    path('panel/add-inventory-city/delete/<int:id>/', Delete_city_inventory.as_view(), name='delete-inv_city'),
    path('panel/inventory/delete/<int:id>/', Delete_Inventory.as_view(), name='delete-inv'),
    path('panel/supplier/', List_Supplier.as_view(), name='link_sup_list'),
    path('panel/supplier/delete/<int:id>/', Delete_Supplier.as_view(), name='delete_sup'),
    path('panel/supplier/add/', add_Supplier.as_view(), name='add_sup'),
    path('panel/supplier/update/<int:id>', Update_Supplier.as_view(), name='link_upd_supp'),
    path('panel/product-variations/', Product_vari_List.as_view(), name='link_list_pro_v'),
    path('panel/product-variations/update/<int:id>', Update_Pro_v.as_view(), name='link_up_pro_v'),
    path('panel/product-variations/delete/<int:id>/', Delete_ProductVariation.as_view(), name='delete-pro_v'),
    path('panel/add-category-product/', add_category_product.as_view(), name='add_cat_pro'),

]
