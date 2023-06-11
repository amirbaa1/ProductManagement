from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm, UserChangeForm


class AdminUser(UserAdmin):
    add_form = SignUpForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'email']


admin.site.register(User, AdminUser)
