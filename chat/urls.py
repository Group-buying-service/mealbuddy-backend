from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:room_id>/", views.chatRoom.as_view(), name="room"),
    path("API/<int:room_id>/", views.PostChatRoomAPI.as_view(), name="roomAPI"),
    path("API/<int:room_id>/user/", views.PostChatRoomUserAPI.as_view())
]