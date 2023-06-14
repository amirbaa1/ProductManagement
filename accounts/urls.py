from django.urls import path

from .views import SignUpView, ProfileView, EditProfile,SittingView,ListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('my_profile/<str:username>/', ProfileView.as_view(), name='my_profile'),
    path('my_profile/edit/<str:username>/', EditProfile.as_view(), name='edit_profile'),
    path('my_profile/edit/<str:username>/setting/',SittingView.as_view(),name='my_setting'),
]
