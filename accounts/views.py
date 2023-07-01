from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, EditProfileForm
from .models import User
from carts.models import Order, OrderItem
from django.contrib import messages


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # go login
    success_message = 'ثبت نام با موفقیت انجام شد. اکانت خود را لاگین کنید'
    template_name = 'registration/sign_up.html'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'اشتباه وارد شده است.دوباره امتحان کنید.')
        return response


class ProfileView(ListView):  # see orderItem in profile
    model = OrderItem
    template_name = 'profile/profile.html'
    context_object_name = 'orders'

    # def get_queryset(self):
    #     return Order.objects.filter(customer=self.request.user)

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-date_order')


class EditProfile(SuccessMessageMixin, UpdateView):
    model = User
    # fields = ['first_name', 'last_name', 'email', 'city']
    form_class = EditProfileForm
    template_name = 'profile/edit_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('my_profile', kwargs={'username': User.username})
    success_message = 'با موفقیت اپدیت شد.'




