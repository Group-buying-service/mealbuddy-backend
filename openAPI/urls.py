from django.urls import path

from . import views

app_name = 'openAPI'

urlpatterns = [
    path("foodchoicer/", views.food_choicer),
    path("weather/", views.weather),
]