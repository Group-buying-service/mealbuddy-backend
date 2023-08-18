from rest_framework.serializers import ModelSerializer
from .models import ChatRoom, ChatMessage

class ChatMessageSerializer(ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = '__all__'
        depth = 1