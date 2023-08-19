from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.views import View

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ChatMessage, ChatRoom, ChatRoomJoin
from .serializer import ChatMessageSerializer

User = get_user_model()


# Create your views here.


def room_join_permission(chat_room, user):
    chat_room_join = ChatRoomJoin.objects.filter(user = user, chatroom=chat_room)
    if chat_room_join.exists():
        return True
    return False


def get_room_join_permission(chat_room, user):
    chat_room_join = ChatRoomJoin.objects.get_or_create(chatroom=chat_room, user=user)


def index(request):
    return render(request, "chat/index.html")


class chatRoomView(View):

    def chat_room_render(self, request, chat_room, user):
        messages = ChatMessage.objects.filter(chatroom = chat_room.pk)
        serialized_messages = ChatMessageSerializer(instance=messages, many=True)
        serialized_user = {"user_id": user.id, "user_username": user.username}
        return render(request, "chat/room.html", {"room_id": chat_room.pk, "messages":serialized_messages.data, "user": serialized_user})
    

    def post(self, request, room_id):
        user = request.user
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
        except ObjectDoesNotExist:
            return redirect('chat:index')
        get_room_join_permission(chat_room, user)
        return self.chat_room_render(request, chat_room, user)
        
    
    def get(self, request, room_id):
        user = request.user
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
            if not room_join_permission(chat_room, user):
                return redirect("chat:index")
        except ObjectDoesNotExist:
            chat_room = ChatRoom.objects.create(owner=user)
            get_room_join_permission(chat_room, user)
        return self.chat_room_render(request, chat_room, user)


# # @APIView
# def room(request, room_id):
#     user = request.user
#     try:
#         chat_room = ChatRoom.objects.get(pk=room_id)
#         if not room_join_permission(chat_room, user):
#             return redirect("chat:index")
#     except ObjectDoesNotExist:
#         chat_room = ChatRoom.objects.create(owner=user)
#         get_room_join_permission(chat_room, user)
#     messages = ChatMessage.objects.filter(chatroom = chat_room.pk)
#     serialized_messages = ChatMessageSerializer(instance=messages, many=True)
#     serialized_user = {"user_id": user.id, "user_username": user.username}
#     return render(request, "chat/room.html", {"room_id": room_id, "messages":serialized_messages.data, "user": serialized_user})

