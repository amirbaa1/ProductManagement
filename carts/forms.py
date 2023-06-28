from django import forms
from products.models import ProductVariation
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=OrderItem.objects.all())

    def __init__(self, *args, **kwargs):
        product_variation_id = kwargs.pop('product_variation_id', None)
        super().__init__(*args, **kwargs)
        if product_variation_id:
            product_variation = ProductVariation.objects.filter(pk=product_variation_id).first()
            if product_variation:
                self.fields['items'].queryset = OrderItem.objects.filter(product_variation=product_variation)

    class Meta:
        model = Order
        fields = ['customer', 'items']


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1)
    product = forms.IntegerField(widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class Status_Update(forms.ModelForm):
    status = forms.ChoiceField(label='تغییر وضعیت سفارش', choices=Order.STATUS_CHOICES,
                               widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ['status']
