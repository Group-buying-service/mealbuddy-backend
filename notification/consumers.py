from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from chat.models import ChatRoomJoin

class NotificationConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.user_id = self.scope['user'].id
        self.group_name = f"notification_{self.user_id}"
        self.chat = list(ChatRoomJoin.objects.filter(is_deleted=False, notification=True, user_id=self.user_id).values_list('chatroom_id','chatroom__post__title'))


        # 룸 그룹 참여
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        
        self.accept()

        self.send_json({"type":"init", "chat": self.chat})


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    def receive_json(self, json_data):
        notification_type = json_data.get('type')
        id = json_data.get('id')

        if notification_type == 'chat':
            self.chat.append(id)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "chat", "id_list": self.chat}
            )

    def notification_send(self, event):
        self.send({**event})