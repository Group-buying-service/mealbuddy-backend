# user > urls.py
from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, DeleteUserView, ChangePasswordView, ProfileUpdateView, UserCheckAPIView

app_name = 'user'

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('changepassword/', ChangePasswordView.as_view(), name='changepassword'),
    path('update/', ProfileUpdateView.as_view(), name='update'),
    path('current/', UserCheckAPIView.as_view()),
]
