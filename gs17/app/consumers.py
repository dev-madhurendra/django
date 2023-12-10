# Topic - Generic Consumer - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
  # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
  def connect(self):
    print('Websocket Connected...')
    self.accept()     # To accept the connection
    # self.close()      # TO reject the connection

  # This handler is called when data received from Client
  # with decoded JSON content
  def receive_json(self, content, **kwargs):
    print('Message received from client...', content)
    print('Type of Message received from client...', type(content))
    # Encode the given content as JSON and send it to the client.
    self.send_json({'message':'Message from Server to Client'})
    # self.close()      # To force-close the connection

  #  This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
  def disconnect(self, close_code):
    print('Websocket Disconnected...', close_code)

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
  # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
  async def connect(self):
    print('Websocket Connected...')
    await self.accept()     # To accept the connection
    # await self.close()      # TO reject the connection

  # This handler is called when data received from Client
  # with decoded JSON content
  async def receive_json(self, content, **kwargs):
    print('Message received from client...', content)
    print('Type of Message received from client...', type(content))
    # Encode the given content as JSON and send it to the client.
    await self.send_json({'message':'Message from Server to Client'})
    # await self.close()      # To force-close the connection

  #  This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
  async def disconnect(self, close_code):
    print('Websocket Disconnected...', close_code)
