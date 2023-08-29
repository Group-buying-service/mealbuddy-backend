# user > urls.py
from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'user'

urlpatterns = [
    path('register', RegistrationAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('current', UserRetrieveUpdateAPIView.as_view()),
]