"""
PINNA
spotify.py

Created by Shota Shimazu on 2018/03/10

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""


class SpotifyWidget():
    
    def __init__(self):
        self._songid = "501qBoW0MQEBySm9c7CcTQ"
        self._height = "380"
        self._width  = "300"


    def html(self):
        """
        Returns:
            - Generated iframe HTML
        """

        return """
<iframe src="https://open.spotify.com/embed/track/{song}" width="{width}" height="{height}" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
        """.format(self._songid, self._height, self._width)


    def info(self, songid, country, height, width):
        """
        Args:
            - songid:string         Apple Music Song ID
            - height:string         Height with unit (e.g, 500px)
            - width:string          Width with unit (e.g, 100%)
        """
        self._songid = songid
        self._height = height
        self._width  = width
