from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import APIView

from .models import ChatMessage, ChatRoom, ChatRoomJoin
from .serializer import ChatMessageSerializer

User = get_user_model()


# Create your views here.


def index(request):
    return render(request, "chat/index.html")


# @APIView
def room(request, room_id):
    user = request.user
    try:
        chat_room = ChatRoom.objects.get(pk=room_id)
    except ObjectDoesNotExist:
        chat_room = ChatRoom.objects.create(owner=user)
    messages = ChatMessage.objects.filter(chatroom = chat_room.pk)
    serialized_messages = ChatMessageSerializer(instance=messages, many=True)
    serialized_user = {"user_id": user.id, "user_username": user.username}
    return render(request, "chat/room.html", {"room_id": room_id, "messages":serialized_messages.data, "user": serialized_user})