from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path('ws/jwc/', consumers.MyJsonWebsocketConsumer.as_asgi()),
  path('ws/ajwc/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]