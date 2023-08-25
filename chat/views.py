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
from .serializer import ChatMessageSerializer, UserListSerializer

User = get_user_model()


# Create your views here.

def index(request):
    return render(request, "chat/APIindex.html")


class chatRoom(View):

    # def chat_room_render(self, request, chat_room, user):
    #     messages = ChatMessage.objects.filter(chatroom = chat_room.pk)
    #     serialized_messages = ChatMessageSerializer(instance=messages, many=True)
    #     serialized_user = {"user_id": user.id, "user_username": user.username}
    #     return render(request, "chat/room.html", {"room_id": chat_room.pk, "messages":serialized_messages.data, "user": serialized_user})
    

    # def post(self, request, room_id):
    #     user = request.user
    #     try:
    #         chat_room = ChatRoom.objects.get(pk=room_id)
    #     except ObjectDoesNotExist:
    #         return redirect('chat:index')
    #     get_room_join_permission(chat_room, user)
    #     return self.chat_room_render(request, chat_room, user)
        
    
    def get(self, request, room_id):
        return render(request, 'chat/APIroom.html')
        # user = request.user
        # try:
        #     chat_room = ChatRoom.objects.get(pk=room_id)
        #     if not room_join_permission(chat_room, user):
        #         return redirect("chat:index")
        # except ObjectDoesNotExist:
        #     chat_room = ChatRoom.objects.create(owner=user)
        #     get_room_join_permission(chat_room, user)
        # return self.chat_room_render(request, chat_room, user)


class ChatRoomAPI(APIView):

    def room_join_permission(self, chat_room, user):
        chat_room_join = ChatRoomJoin.objects.filter(user=user, chatroom=chat_room, is_deleted=False)
        if chat_room_join.exists():
            return True
        return False


    def get_room_join_permission(self, chat_room, user):
        if not user.username in chat_room.blacklist:
            chat_room_join, created =  ChatRoomJoin.objects.get_or_create(chatroom=chat_room, user=user)
            if not created:
                chat_room_join.is_deleted = False
                chat_room_join.save()
            return chat_room_join
        return False

    def chat_room_render(self, chat_room, user):
        # user_list = chat_room.room_join.all()

        messages = ChatMessage.objects.filter(chatroom = chat_room.pk)
        serialized_messages = ChatMessageSerializer(instance=messages, many=True)
        serialized_user = {"user_id": user.id, "user_username": user.username}
        return Response({"room_id": chat_room.pk, "messages":serialized_messages.data, "user": serialized_user}, status=status.HTTP_200_OK)


class PostChatRoomAPI(ChatRoomAPI):

    # 채팅방 정보 반환
    def get(self, request, room_id):
        user = request.user
        # user = User.objects.get(pk=1)
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
            if chat_room.is_deleted:
                return Response("삭제된 채팅방입니다.", status=status.HTTP_400_BAD_REQUEST)
            if not self.room_join_permission(chat_room, user):
                return Response("채팅방에 접근할 권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            return Response("채팅방이 존재하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
        return self.chat_room_render(chat_room, user)
    
    # 채팅방 접근 권한 부여 및 채팅방 생성
    def post(self, request, room_id):
        user = request.user
        # user = User.objects.get(pk=1)
        try:
            chat_room = ChatRoom.objects.get(pk=room_id)
        except ObjectDoesNotExist:
            chat_room = ChatRoom.objects.create(owner=user)
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
        if user == chat_room.owner:
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
        if user!=chat_room.owner:
            return Response("권한이 없습니다.", status=status.HTTP_400_BAD_REQUEST)
        try:
            chat_room_join = ChatRoomJoin.objects.get(user__username=target_username, chatroom_id=room_id)
        except ObjectDoesNotExist as e:
            print(e)
            return Response("올바르지 않은 요청입니다.", status=status.HTTP_400_BAD_REQUEST)

        chat_room.blacklist.append(target_username)
        chat_room.save()
        chat_room_join.is_deleted = True
        chat_room_join.save()
        return Response("해당 유저를 강퇴하였습니다.", status=status.HTTP_202_ACCEPTED)


    # 방 나가기
    def delete(self, request, room_id):
        user = request.user
        try:
            chat_room_join = ChatRoomJoin.objects.get(user=user, chatroom_id=room_id)
        except ObjectDoesNotExist:
            return Response("올바르지 않은 요청입니다.", status=status.HTTP_400_BAD_REQUEST)
        chat_room_join.is_deleted = True
        chat_room_join.save()
        return Response("채팅방에서 퇴장하였습니다.", status=status.HTTP_202_ACCEPTED)

