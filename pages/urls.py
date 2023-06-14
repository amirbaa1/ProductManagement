from django.contrib import admin
from django.urls import path

from products.views import HomePageView
from .views import AboutPage, ContactUsPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact_us/', ContactUsPage.as_view(), name='contact_us'),

    path('categories/<int:pk>/', HomePageView.as_view(), name='categories_list'),
]
