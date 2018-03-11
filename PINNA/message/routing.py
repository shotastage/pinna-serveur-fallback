"""
StreetStory Serveur
routing.py

Created by Shota Shimazu on 2018/03/04

Copyright (c) 2018 Labbiness, Inc All Rights Reserved.
Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Cloud System License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""

from django.conf.urls import re_path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.consumers import AdminChatConsumer, PublicChatConsumer
from aprs_news.consumers import APRSNewsConsumer

application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path("^chat/admin/$", AdminChatConsumer),
            re_path("^chat/$", PublicChatConsumer),
        ])
    ),

    # Using the third-party project frequensgi, which provides an APRS protocol
    "aprs": APRSNewsConsumer,

})
