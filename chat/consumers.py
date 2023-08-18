import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import ChatRoom, ChatRoomJoin, ChatMessage
from .serializer import ChatMessageSerializer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_data = text_data_json['user']
        room_id = text_data_json['room_id']
        
        chatMessage_queryset = ChatMessage.objects.create(message=message, user_id=user_data['user_id'], chatroom_id = room_id)
        # print(chatMessage_queryset)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": serialized_message.data}
        )

    # Receive message from room group
    def chat_message(self, event):
        # print(event)
        # event_json = json.loads(event)
        message = event["message"]["message"]
        user = event["message"]["user"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "user": user}))