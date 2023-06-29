from django import forms
from .models import ProductVariation, ProductCategory, Supplier, City, Inventory, InventoryProduct


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


class Form_add_cityInventory(forms.ModelForm):
    cityId = forms.ModelChoiceField(label='شهر', queryset=City.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Inventory
        fields = ['cityId']


class Form_add_Inventory_product(forms.ModelForm):
    productId = forms.ModelChoiceField(label='نام محصول', queryset=ProductVariation.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='تعداد', widget=forms.TextInput(attrs={'class': 'form-control'}))
    inventoryId = forms.ModelChoiceField(label='شهر', queryset=Inventory.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = InventoryProduct
        fields = ['productId','quantity','inventoryId']
