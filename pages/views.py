from django.views.generic import TemplateView, ListView

from products.models import Inventory, InventoryProduct, Product, ProductVariation


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactUsPage(TemplateView):
    template_name = 'contact_us.html'


