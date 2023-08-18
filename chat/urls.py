from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_id>/", views.room, name="room"),
]