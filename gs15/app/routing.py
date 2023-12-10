from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path('ws/wsc/<str:groupkaname>/', consumers.MyWebsocketConsumer.as_asgi()),
  path('ws/awsc/<str:groupkaname>/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]