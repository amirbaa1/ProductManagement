from django.views.generic import TemplateView, ListView


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactUsPage(TemplateView):
    template_name = 'contact_us.html'
