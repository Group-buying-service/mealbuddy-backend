import redis
import json
from decouple import config

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer

from .models import ChatMessage
from .serializer import ChatMessageSerializer, UserSerializer


userlist_redis_client = redis.StrictRedis(host=config('REDIS_HOST'), port=config('REDIS_PORT'), db=0)


class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"
        self.user = self.scope['user']
        self.userlist = userlist_redis_client.get(f'chat_userlist_{self.room_id}')
        if self.userlist:
            self.userlist = set(json.loads(self.userlist))
            self.userlist.add(self.user.id)
        else:
            self.userlist = set()
            self.userlist.add(self.user.id)
        userlist_redis_client.set(f'chat_userlist_{self.room_id}', json.dumps(list(self.userlist)))

        # 룸 그룹 참여
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.user.connect", "user_id":self.user.id}
        )


    def disconnect(self, close_code):
        self.userlist.remove(self.user.id)
        userlist_redis_client.set(f'chat_userlist_{self.room_id}', json.dumps(list(self.userlist)))
        # Leave room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.user.disconnect", "user_id":self.user.id}
        )

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # WS 에서 메세지 받아옴.
    def receive_json(self, json_data):

        message = json_data["message"]
        
        chatMessage_queryset = ChatMessage.objects.create(message=message, user=self.user, chatroom_id = self.room_id)
        serialized_message = ChatMessageSerializer(instance=chatMessage_queryset)

        # 그룹에게 받아온 메세지 전송
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": serialized_message.data}
        )

    # 메세지가 업데이트되면 룸 멤버에게 메세지 전송
    def chat_message(self, event):
        self.send_json({**event})

    def chat_user_join(self, event):
        self.send_json({**event})

    def chat_user_leave(self, event):
        self.send_json({**event})

    def chat_room_deleted(self, event):
        custom_code = 4040
        self.close(code=custom_code)

    def chat_user_connect(self, event):
        self.userlist = set(json.loads(userlist_redis_client.get(f'chat_userlist_{self.room_id}')))

    def chat_user_disconnect(self, event):
        self.userlist = set(json.loads(userlist_redis_client.get(f'chat_userlist_{self.room_id}')))


