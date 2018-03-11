"""
StreetStory Serveur
urls.py

Created by Shota Shimazu on 2018/2/11

Copyright (c) 2018 Labbiness, Inc All Rights Reserved.
Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Software License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""

from django.urls import include, path
from . import views

urlpatterns = [
    path(r'^$',  views.about, name='about'),
    path(r'^new/$', views.new_room, name='new_room'),
    path(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
