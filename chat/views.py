from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.views import View

from rest_framework.decorators import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ChatMessage, ChatRoom, ChatRoomJoin
from .serializer import ChatMessageSerializer, UserListSerializer, UserSerializer, ChatRoomPostSerializer

User = get_user_model()


# Create your views here.

def index(request):
    return render(request, "chat/APIindex.html")


def chatRoom(request, room_id):
    return render(request, 'chat/APIroom.html')



class ChatRoomAPI(APIView):

    def room_join_permission(self, chat_room, user):
        chat_room_join = ChatRoomJoin.objects.filter(user=user, chatroom=chat_room, is_deleted=False)
        if chat_room_join.exists():
            return True
        return False

    def get_room_join_permission(self, chat_room, user):
        if not user.username in chat_room.blacklist:
            post = chat_room.post
            if ChatRoomJoin.objects.filter(chatroom=chat_room, is_deleted=False).count() < post.target_number:
                chat_room_join, created =  ChatRoomJoin.objects.get_or_create(chatroom=chat_room, user=user)
                post.join_number = post.join_number + 1
                #post.recruited_users.add(user)
                post.save()
                if not created:
                    chat_room_join.is_deleted = False
                    chat_room_join.save()
                return chat_room_join
        return False

    def chat_room_render(self, chat_room, user):
        messages = ChatMessage.objects.filter(chatroom = chat_room.pk)
        serialized_messages = ChatMessageSerializer(instance=messages, many=True)
        post = chat_room.post
        serialized_post = ChatRoomPostSerializer(instance=post)
        serialized_user = UserSerializer(instance=user)
        return Response({"messages":serialized_messages.data, "user": serialized_user.data, **serialized_post.data}, status=status.HTTP_200_OK)


class PostChatRoomAPI(ChatRoomAPI):

    # 채팅방 정보 반환
    def get(self, request, room_id):
        user = request.user
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
            if chat_room.is_deleted:
                return Response("삭제된 채팅방입니다.", status=status.HTTP_400_BAD_REQUEST)
            if not self.room_join_permission(chat_room, user):
                return Response("채팅방에 접근할 권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        return self.chat_room_render(chat_room, user)
    
    # 채팅방 접근 권한 부여
    def post(self, request, room_id):
        user = request.user
        # if post_id:
        #     try:
        #         chat_room = ChatRoom.objects.create(post_id=post_id, owner=user)
        #     except:
        #         return Response("이미 존재하는 채팅방입니다", status=status.HTTP_400_BAD_REQUEST)
        # else:
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        if self.get_room_join_permission(chat_room, user):
            return self.chat_room_render(chat_room, user)
        return Response("인원수가 가득 찼거나 밴 당한 상태입니다", status=status.HTTP_400_BAD_REQUEST)

    # 채팅방 삭제
    def delete(self, request, room_id):
        user = request.user
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        if user == chat_room.post.writer:
            chat_room.is_deleted = True
            chat_room.save()
            return Response("채팅방이 삭제되었습니다.", status=status.HTTP_202_ACCEPTED)
        return Response("채팅방을 삭제할 권한이 없습니다.", status=status.HTTP_400_BAD_REQUEST)


class PostChatRoomUserAPI(APIView):

    # 유저리스트 정보 받기
    def get(self, request, room_id):
        try:
            userlist_qs = ChatRoomJoin.objects.filter(chatroom_id=room_id, is_deleted=False)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        
        userlist_serailzer = UserListSerializer(userlist_qs, many=True)

        return Response(userlist_serailzer.data, status=status.HTTP_200_OK)


    # 유저 강퇴
    def post(self, request, room_id):
        user = request.user
        target_username = request.data.get('target_username')
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        if user!=chat_room.post.writer:
            return Response("권한이 없습니다.", status=status.HTTP_400_BAD_REQUEST)
        try:
            chat_room_join = ChatRoomJoin.objects.get(user__username=target_username, chatroom_id=room_id)
        except ObjectDoesNotExist:
            return Response("올바르지 않은 요청입니다.", status=status.HTTP_400_BAD_REQUEST)

        chat_room.blacklist.append(target_username)
        chat_room.save()
        chat_room_join.is_deleted = True
        chat_room_join.save()
        post = chat_room.post
        post.join_number = post.join_number - 1
        #post.recruited_users.remove(user)
        post.save()
        return Response("해당 유저를 강퇴하였습니다.", status=status.HTTP_202_ACCEPTED)


    # 방 나가기
    def delete(self, request, room_id):
        user = request.user
        try:
            chat_room_join = ChatRoomJoin.objects.get(user=user, chatroom_id=room_id)
        except ObjectDoesNotExist:
            return Response("올바르지 않은 요청입니다.", status=status.HTTP_400_BAD_REQUEST)
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        chat_room_join.is_deleted = True
        chat_room_join.save()
        post = chat_room.post
        post.join_number = post.join_number - 1
        #post.recruited_users.remove(user)
        post.save()
        return Response("채팅방에서 퇴장하였습니다.", status=status.HTTP_202_ACCEPTED)

