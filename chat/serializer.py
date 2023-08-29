from rest_framework.serializers import ModelSerializer
from .models import ChatRoom, ChatMessage, ChatRoomJoin

class ChatMessageSerializer(ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = '__all__'
        depth = 1


class UserListSerializer(ModelSerializer):

    class Meta:
        model = ChatRoomJoin
        fields = ['user']
        depth = 1