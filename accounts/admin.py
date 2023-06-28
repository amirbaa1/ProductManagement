from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm, UserChangeForm


##@admin.register(User)
class AdminUser(UserAdmin):
    add_form = SignUpForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_active']


admin.site.register(User, AdminUser)
