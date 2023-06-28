# TODO form create product
from django import forms
from .models import ProductVariation, ProductCategory, Supplier, City


class Form_add_product(forms.ModelForm):
    productId = forms.ModelChoiceField(label='دسته بندی', queryset=ProductCategory.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(label='نام محصول', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Supplier = forms.ModelMultipleChoiceField(label='تامین کننده', queryset=Supplier.objects.all(),
                                              widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='قیمت', widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='تعداد', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cityId = forms.ModelChoiceField(label='شهر', queryset=City.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ProductVariation
        fields = ['productId', 'name', 'Supplier', 'price', 'quantity', 'cityId']
