"""
StreetStory Serveur
message_type.py

Created by Jimbo Kazuyuki on 2018/03/08

Copyright (c) 2018 Labbiness, Inc All Rights Reserved.
Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Cloud System License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""


NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS = False

MSG_TYPE_MESSAGE = 0  # For standard messages
MSG_TYPE_IMAGE = 1  # For yellow messages

MESSAGE_TYPES_CHOICES = (
    (MSG_TYPE_MESSAGE, 'MESSAGE'),
    (MSG_TYPE_IMAGE, 'IMAGE'),
)

MESSAGE_TYPES_LIST = [
    MSG_TYPE_MESSAGE,
    MSG_TYPE_IMAGE,

]

