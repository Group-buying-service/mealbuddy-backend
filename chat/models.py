from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class ChatRoom(models.Model):

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # post = models.ForeignKey(to='Chat', on_delete=models.CASCADE)

    class Meta:
        db_table = "chatRoom"


class ChatRoomJoin(models.Model):

    chatroom = models.ForeignKey(to="ChatRoom", on_delete=models.CASCADE, related_name="room_join", db_column="chatroom_id")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chatRoomJoin"


class ChatMessage(models.Model):

    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey(to="ChatRoom", on_delete=models.CASCADE, related_name="chat_room", db_column="chatroom_id")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user", db_column="user_id")

    class Meta:
        db_table = "chatMessage"