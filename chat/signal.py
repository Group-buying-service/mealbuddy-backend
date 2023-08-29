from .models import ChatRoom, ChatRoomJoin, ChatMessage
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channels_layer = get_channel_layer()


@receiver(post_save, sender=ChatRoomJoin)
def chatroomjoin_created(sender, instance, created, **kwargs):
    if created or (not created and not instance.is_deleted):
        chat_group_name = f"chat_{instance.chatroom.pk}"
        async_to_sync(channels_layer.group_send)(
            chat_group_name,
            {
                "type": "chat.user.join",
                "user": instance.user.username,
            }
        )


@receiver(post_save, sender=ChatRoomJoin)
def chatroomjoin_deleted(sender, instance, created, **kwargs):
    if not created and instance.is_deleted:
        chat_group_name = f"chat_{instance.chatroom.pk}"
        async_to_sync(channels_layer.group_send)(
            chat_group_name,
            {
                "type": "chat.user.leave",
                "user": instance.user.username,
            }
        )



@receiver(post_save, sender=ChatRoom)
def chatroom_deleted(sender, instance, created, **kwargs):
    if not created and instance.is_deleted:
        chat_group_name = f"chat_{instance.pk}"
        async_to_sync(channels_layer.group_send)(
            chat_group_name,
            {
                "type": "chat.room.deleted",
            }
        )