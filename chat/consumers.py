import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer

from .models import ChatRoom, ChatRoomJoin, ChatMessage
from .serializer import ChatMessageSerializer


class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"
        self.user = self.scope['user']

        # 룸 그룹 참여
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )


    # WS 에서 메세지 받아옴.
    def receive_json(self, json_data):
        message = json_data["message"]
        # user_data = json_data['user']
        # room_id = json_data['room_id']

        # if str(room_id) != self.room_id:
        #     self.send_json({
        #         "type": 'chat.error.permission',
        #         "message": '권한이 없는 요청입니다.'
        #     })
        #     self.close()
        
        chatMessage_queryset = ChatMessage.objects.create(message=message, user=self.user, chatroom_id = self.room_id)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)

        # 그룹에게 받아온 메세지 전송
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": serialized_message.data}
        )

    # 메세지가 업데이트되면 룸 멤버에게 메세지 전송
    def chat_message(self, event):
        event_type = event["type"]
        message = event["message"]["message"]
        user = event["message"]["user"]

        # Send message to WebSocket
        self.send_json({"type": event_type, "message": message, "user": user})


    def chat_user_join(self, event):
        event_type = event["type"]
        user = event["user"]
        chatMessage_queryset = ChatMessage.objects.create(message=f"{user} 님이 입장했습니다.", chatroom_id = self.room_id)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)
        self.send_json({"type": event_type, "message": serialized_message.data})


    def chat_user_leave(self, event):
        event_type = event["type"]
        user = event["user"]
        chatMessage_queryset = ChatMessage.objects.create(message=f"{user} 님이 퇴장했습니다.", chatroom_id = self.room_id)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)
        self.send_json({"type": event_type, "message": serialized_message.data})


    def chat_room_deleted(self, event):
        custom_code = 4040
        self.close(code=custom_code)


