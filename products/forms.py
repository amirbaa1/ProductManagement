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
        fields = ['productId', 'quantity', 'inventoryId']


class Form_Update_Supplier(forms.ModelForm):
    name = forms.CharField(label='نام محصول', widget=forms.TextInput(attrs={'class': 'form-control'}))

    contactInfo = forms.IntegerField(label='شماره تلفن', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Supplier
        fields = ['name', 'contactInfo']


class Form_Update_ProV(forms.ModelForm):
    # productId = forms.ModelChoiceField(label='نام محصول', queryset=ProductVariation.objects.all(), required=False,
    #                                    widget=forms.Select(attrs={'class': 'form-control', 'disabled': True}))
    name = forms.CharField(label='نام محصول', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Supplier = forms.ModelMultipleChoiceField(label='تامین کننده', queryset=Supplier.objects.all(),
                                              widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='قیمت', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='تعداد', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cityId = forms.ModelChoiceField(label='شهر', queryset=City.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}), )
    text = forms.CharField(label='توضیحات', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = ProductVariation
        fields = ['name', 'Supplier', 'price', 'quantity', 'cityId', 'text']


class Form_add_Supplier(forms.ModelForm):
    name = forms.CharField(label='نام تامین کننده', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    contactInfo = forms.IntegerField(label='شماره تلفن', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Supplier
        fields = ['name', 'contactInfo']


class Form_add_category_product(forms.ModelForm):
    name = forms.CharField(label='نام تامین کننده', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ProductCategory
        fields = ['name']
