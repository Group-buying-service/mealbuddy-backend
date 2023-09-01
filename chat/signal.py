from .models import ChatRoom, ChatRoomJoin, ChatMessage
from .serializer import ChatMessageSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channels_layer = get_channel_layer()


@receiver(post_save, sender=ChatRoomJoin)
def chatroomjoin_created(sender, instance, created, **kwargs):
    if created or (not created and not instance.is_deleted):
        chat_group_name = f"chat_{instance.chatroom.pk}"
        chatMessage_queryset = ChatMessage.objects.create(message=f"{instance.user.username} 님이 입장했습니다.", chatroom_id = instance.chatroom.pk)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)
        async_to_sync(channels_layer.group_send)(
            chat_group_name,
            {
                "type": "chat.user.join",
                "user": instance.user.username,
                "message": serialized_message.data,
            }
        )


@receiver(post_save, sender=ChatRoomJoin)
def chatroomjoin_deleted(sender, instance, created, **kwargs):
    if not created and instance.is_deleted:
        chat_group_name = f"chat_{instance.chatroom.pk}"
        chatMessage_queryset = ChatMessage.objects.create(message=f"{instance.user.username} 님이 퇴장했습니다.", chatroom_id = instance.chatroom.pk)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)
        async_to_sync(channels_layer.group_send)(
            chat_group_name,
            {
                "type": "chat.user.leave",
                "user": instance.user.username,
                "message": serialized_message.data,
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