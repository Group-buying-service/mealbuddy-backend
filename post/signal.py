from chat.models import ChatRoom, ChatRoomJoin
from .models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        chat_room = ChatRoom.objects.create(post = instance)
        chat_room_join = ChatRoomJoin.objects.create(chatroom = chat_room, user=instance.writer)