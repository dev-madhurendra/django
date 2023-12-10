# Topic - Generic Consumer - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
# Chat App with Dynamic Group Name
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
  # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
  def connect(self):
    print('Websocket Connected...')
    print("Channel Layer", self.channel_layer)
    print("Channel Name", self.channel_name)
    self.group_name = self.scope['url_route']['kwargs']['groupkaname']
    print("Group Name:", self.group_name)
    async_to_sync(self.channel_layer.group_add)(
      self.group_name,
      self.channel_name
    )
    self.accept()     # To accept the connection

  # This handler is called when data received from Client
  # with decoded JSON content
  def receive_json(self, content, **kwargs):
    print('Message received from client...', content)
    async_to_sync(self.channel_layer.group_send)(
      self.group_name,
      {
        'type': 'chat.message',
        'message':content['msg']
      }
    )

  def chat_message(self, event):
    print("Event...", event)
    self.send_json({
      'message':event['message']
    })

  #  This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
  def disconnect(self, close_code):
    print('Websocket Disconnected...', close_code)
    print("Channel Layer", self.channel_layer)
    print("Channel Name", self.channel_name)
    async_to_sync(self.channel_layer.group_discard)(
      self.group_name,
      self.channel_name
    )

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
  # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
  async def connect(self):
    print('Websocket Connected...')
    print("Channel Layer", self.channel_layer)
    print("Channel Name", self.channel_name)
    self.group_name = self.scope['url_route']['kwargs']['groupkaname']
    print("Group Name:", self.group_name)
    await self.channel_layer.group_add(
      self.group_name,
      self.channel_name
    )
    await self.accept()     # To accept the connection

  # This handler is called when data received from Client
  # with decoded JSON content
  async def receive_json(self, content, **kwargs):
    print('Message received from client...', content)
    await self.channel_layer.group_send(
      self.group_name,
      {
        'type': 'chat.message',
        'message':content['msg']
      }
    )

  async def chat_message(self, event):
    print("Event...", event)
    await self.send_json({
      'message':event['message']
    })

  #  This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
  async def disconnect(self, close_code):
    print('Websocket Disconnected...', close_code)
    print("Channel Layer", self.channel_layer)
    print("Channel Name", self.channel_name)
    await self.channel_layer.group_discard(
      self.group_name,
      self.channel_name
    )