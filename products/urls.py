from django.urls import path
from .views import ProductVariation_Detail

urlpatterns = [
    path('pr-<int:pk>/', ProductVariation_Detail.as_view(), name='pro_v')
]
