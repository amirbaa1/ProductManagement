from django.urls import path
from .views import ProductVariation_Detail, CreateProduct

urlpatterns = [
    path('pr-<int:pk>/', ProductVariation_Detail.as_view(), name='pro_v'),
    path('panel/add-product/', CreateProduct.as_view(), name='add_product')
]
