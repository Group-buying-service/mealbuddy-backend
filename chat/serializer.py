from rest_framework.serializers import ModelSerializer
from .models import ChatRoom, ChatMessage, ChatRoomJoin
from post.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ChatRoomPostSerializer(ModelSerializer):

    writer = UserSerializer()

    class Meta:
        model = Post
        fields = ['title', 'target_number', 'join_number', 'writer']
        depth = 1


class ChatMessageSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ChatMessage
        fields = '__all__'
        depth = 1


class UserListSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ChatRoomJoin
        fields = ['user']
        depth = 1