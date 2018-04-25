"""
PINNA
applemusic.py

Created by Shota Shimazu on 2018/03/10

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

class AppleMusicWidget():
    
    def __init__(self):
        self._country = "jp"
        self._songid = "1167463173"
        self._height = "500px"
        self._width  = "100%"


    def html(self):
        """
        Returns:
            - Generated iframe HTML
        """

        return """
<iframe src="https://tools.applemusic.com/embed/v1/album/{id}?country={country}" height="{height}" width="{width}" frameborder="0"></iframe>
        """.format(self._songid, self._country, self._height, self._width)


    def info(self, songid, country, height, width):
        """
        Args:
            - songid:string         Apple Music Song ID
            - country:string        Country Code (e.g, jp)
            - height:string         Height with unit (e.g, 500px)
            - width:string          Width with unit (e.g, 100%)
        """
        self._country = country
        self._songid = songid
        self._height = height
        self._width  = width
