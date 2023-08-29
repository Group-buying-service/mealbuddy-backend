# user > urls.py
from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView, LogoutView, DeleteUserView, ChangePasswordView

app_name = 'user'

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('changepassword/', ChangePasswordView .as_view(), name='changepassword'),
]

