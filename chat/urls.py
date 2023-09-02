from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path("<int:room_id>/", views.PostChatRoomAPI.as_view(), name="roomAPI"),
    path("<int:room_id>/user/", views.PostChatRoomUserAPI.as_view()),
    path("<int:room_id>/user/ban/", views.PostChatRoomBanAPI),
]