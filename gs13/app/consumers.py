# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer
# Real-time Data Example
# Real-time Data Example with Front End

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio

class MyWebsocketConsumer(WebsocketConsumer):
  # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
  def connect(self):
    print('Websocket Connected...')
    self.accept()     # To accept the connection
  
  # This handler is called when data received from Client
  def receive(self, text_data=None, bytes_data=None):
    print('Message Received from Client...', text_data)
    for i in range(20):
      self.send(text_data=str(i))   # To send data to client
      sleep(1)


  # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
  def disconnect(self, close_code):
    print('Websocket Disconnected...', close_code)

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
  # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
  async def connect(self):
    print('Websocket Connected...')
    await self.accept()     # To accept the connection
  
  # This handler is called when data received from Client
  async def receive(self, text_data=None, bytes_data=None):
    print('Message Received from Client...', text_data)
    for i in range(20):
      await self.send(text_data=str(i))   # To send data to client
      await asyncio.sleep(1)

  # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
  async def disconnect(self, close_code):
    print('Websocket Disconnected...', close_code)