"""
StreetStory Serveur
models.py

Created by Shota Shimazu on 2018/2/11

Copyright (c) 2018 Labbiness, Inc All Rights Reserved.
Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Software License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""

from django.db import models

from django.db import models


class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id