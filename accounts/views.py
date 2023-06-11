from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from .forms import SignUpForm
from .models import User
from carts.models import Order, OrderItem


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'registration/sign_up.html'


class ProfileView(ListView):
    model = OrderItem
    template_name = 'profile/profile.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-date_order')


class EditProfile(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'city']
    template_name = 'profile/edit_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class SittingView(TemplateView):
    template_name = 'profile/setting.html'

# class ListOrder(ListView): # two address in profile ??
#     model = OrderItem
#     template_name = 'profile/profile.html'
#     context_object_name = 'orders'
