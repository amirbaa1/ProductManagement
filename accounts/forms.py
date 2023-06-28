from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from products.models import City
from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='نام کاربر', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control custom-float-left'}))
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(label='شهر', queryset=City.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'city']


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='ایمیل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(label='شهر', queryset=City.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'city']
