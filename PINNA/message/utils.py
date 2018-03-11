"""
StreetStory Serveur
utils.py

Created by Jimbo Kazuyuki on 2018/03/08

Copyright (c) 2018 Labbiness, Inc All Rights Reserved.
Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Cloud System License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""

from channels.db import database_sync_to_async

from .exceptions import ClientError
from .models import Room


# This decorator turns this function from a synchronous function into an async one
# we can call from our async consumers, that handles Django DBs correctly.
# For more, see http://channels.readthedocs.io/en/latest/topics/databases.html
@database_sync_to_async
def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    if not user.is_authenticated:
        raise ClientError("USER_HAS_TO_LOGIN")
    # Find the room they requested (by ID)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise ClientError("ROOM_INVALID")
    # Check permissions
    if room.staff_only and not user.is_staff:
        raise ClientError("ROOM_ACCESS_DENIED")
    return room