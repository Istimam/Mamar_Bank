from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

urlpatterns = [
path('register/', UserRegistrationView.as_view(), name='register'),
path('login/', UserLoginView.as_view(), name='login'),
path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
path('logout/', UserLogoutView.as_view(), name='logout'),
]