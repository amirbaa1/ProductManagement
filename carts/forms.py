from django import forms
from products.models import ProductVariation, Inventory, InventoryProduct
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=OrderItem.objects.all())

    def __init__(self, *args, **kwargs):
        product_variation = kwargs.pop('product_variation', None)
        super().__init__(*args, **kwargs)
        if product_variation:
            self.fields['items'].queryset = OrderItem.objects.filter(product_variation=product_variation)

    class Meta:
        model = Order
        fields = ['customer', 'items']

    # def __init__(self, *args, **kwargs):
    #     product_variation_id = kwargs.pop('product_variation_id', None)
    #     super().__init__(*args, **kwargs)
    #     if product_variation_id:
    #         product_variation = ProductVariation.objects.filter(pk=product_variation_id).first()
    #         if product_variation:
    #             self.fields['items'].queryset = OrderItem.objects.filter(product_variation=product_variation)

    class Meta:
        model = Order
        fields = ['customer', 'items']


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1)
    product_variation_id = forms.IntegerField(widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class InventoryForm(forms.Form):
    inventory = forms.ModelChoiceField(queryset=Inventory.objects.all(), empty_label=None, label='انبار')

    # class Meta:
    #     model = InventoryProduct
    #     field = ['inventoryId']
