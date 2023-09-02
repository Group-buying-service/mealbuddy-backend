from rest_framework import serializers, viewsets
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

# Serializer 정의
class PostSerializer(serializers.ModelSerializer):
    writer = WriterSerializer(read_only=True)
    address = serializers.CharField(source='writer.profile.address', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        chatroom_id = instance.chatroom.id
        rep['chat_id'] = chatroom_id
        return rep


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'