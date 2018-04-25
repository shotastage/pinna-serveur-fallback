"""
PINNA Serveur
exceptions.py

Created by Jimbo Kazuyuki on 2018/03/08

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Cloud System License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""


class ClientError(Exception):
    """
    Custom exception class that is caught by the websocket receive()
    handler and translated into a send back to the client.
    """
    def __init__(self, code):
        super().__init__(code)
        self.code = code
