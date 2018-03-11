from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer


from .exceptions import ClientError
from .utils import get_room_or_error
from .consts import MESSAGE_TYPES_CHOICES


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.accept()
        self.rooms = set()

    async def receive_json(self, content):
        command = content.get("command", None)
        try:
            if command == "init":
                await self.init_room(content["room"])

            elif command == "leave":
                await self.leave_room(content["room"])

            elif command == "send":
                mes = content["contents"].get("message",None)
                try:                   
                    await self.send_room(content["room"], mes, content["contents_type"])
                except ClientError as e:
                    await self.send_json({"error": e.code})

        except ClientError as e:
            await self.send_json({"error": e.code})

    async def disconnect(self, code):

        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
            except ClientError:
                pass

    async def init_room(self, room_id):

        room = await get_room_or_error(room_id, self.scope["user"])

        self.rooms.add(room_id)
        
        # Add them to the group so they get room messages
        await self.channel_layer.group_add(
            room.group_name,
            self.channel_name,
        )


    # perhaps this function will be not used
    async def leave_room(self, room_id):

        room = await get_room_or_error(room_id, self.scope["user"])

        self.rooms.discard(room_id)
        # discard them to the group so they get room messages
        await self.channel_layer.group_discard(
            room.group_name,
            self.channel_name,
        )


    async def send_room(self, room_id, message, contents_type):

        if room_id not in self.rooms:
            raise ClientError("ROOM_ACCESS_DENIED")

        room = await get_room_or_error(room_id, self.scope["user"])

        await self.channel_layer.group_send(
            room.group_name,
            {
                "type": "chat.message",
                "room_id": room_id,
                "username": self.scope["user"].username,
                "contents_type" : contents_type,
                "message": message,
            }
        )

    async def chat_join(self, event):

        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": event["room_id"],
                "username": event["username"],
            },
        )

    async def chat_leave(self, event):

        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": event["room_id"],
                "username": event["username"],
            },
        )

    async def chat_message(self, event):

        await self.send_json(
            {
                "command" : "send",
                "room": event["room_id"],
                "from": event["username"],
                "contents_type" : event["contents_type"],
                "contents": {
                    "message": event["message"],
                },
            },
        )
