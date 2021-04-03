# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Thread
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        friend = self.scope['url_route']['kwargs']['room_name']
        friend = sync_to_async(User.objects.get)(id=friend)
        me = sync_to_async(User.objects.get)(id=1)
        if Thread.objects.filter(user1=me, user2=friend).exists() or Thread.objects.filter(user1=friend, user2=me).exists():
            if Thread.objects.filter(user1=me, user2=friend).exists():
                thread = await Thread.objects.get(user1=me, user2=friend)
            else:
                thread = await Thread.objects.get(user1=friend, user2=me)
            self.room_name = thread
        else:
            thread = await Thread.objects.create(user1=me, user2=friend)
            self.room_name = thread.id
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))