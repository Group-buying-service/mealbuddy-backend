from django.urls import path

from . import views

app_name = 'foodchoicer'

urlpatterns = [
    path("", views.index, name="foodchoicer"),
    path("API/", views.food_choicer)
]