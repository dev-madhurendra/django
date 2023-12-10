# Topic - Chat App with Static Group Name
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
class MySyncConsumer(SyncConsumer):
  def websocket_connect(self, event):
    print('Websocket Connected...', event)
    print("Channel Layer...", self.channel_layer)   # get default channel layer from a project
    print("Channel Name...", self.channel_name)   # get channel Name
    #  add a channel to a new or existing group
    async_to_sync(self.channel_layer.group_add)(
      'programmers',      # group name
      self.channel_name
      )
    self.send({
      'type':'websocket.accept'
    })

  def websocket_receive(self, event):
    print('Message Received from Client...', event['text'])
    print('Type of Message Received from Client...', type(event['text']))
    async_to_sync(self.channel_layer.group_send)(
      'programmers', 
      {
        'type': 'chat.message',
        'message':event['text']
      }
    )
  
  def chat_message(self, event):
    print('Event...', event)
    print('Actual Data...', event['message'])
    print('Type of Actual Data...', type(event['message']))
    self.send({
      'type': 'websocket.send',
      'text': event['message']
    })


  def websocket_disconnect(self, event):
    print('Websocket Disconnected...', event)
    print("Channel Layer...", self.channel_layer)   # get default channel layer from a project
    print("Channel Name...", self.channel_name)   # get channel Name
    async_to_sync(self.channel_layer.group_discard)(
      'programmers', 
      self.channel_name
      )
    raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
  async def websocket_connect(self, event):
    print('Websocket Connected...', event)
    print("Channel Layer...", self.channel_layer)   # get default channel layer from a project
    print("Channel Name...", self.channel_name)   # get channel Name
    #  add a channel to a new or existing group
    await self.channel_layer.group_add(
      'programmers',      # group name
      self.channel_name
      )
    await self.send({
      'type':'websocket.accept'
    })

  async def websocket_receive(self, event):
    print('Message Received from Client...', event['text'])
    print('Type of Message Received from Client...', type(event['text']))
    await self.channel_layer.group_send(
      'programmers', 
      {
        'type': 'chat.message',
        'message':event['text']
      }
    )
  
  async def chat_message(self, event):
    print('Event...', event)
    print('Actual Data...', event['message'])
    print('Type of Actual Data...', type(event['message']))
    await self.send({
      'type': 'websocket.send',
      'text': event['message']
    })


  async def websocket_disconnect(self, event):
    print('Websocket Disconnected...', event)
    print("Channel Layer...", self.channel_layer)   # get default channel layer from a project
    print("Channel Name...", self.channel_name)   # get channel Name
    await self.channel_layer.group_discard(
      'programmers', 
      self.channel_name
      )
    raise StopConsumer()
  