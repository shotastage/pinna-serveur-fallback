"""
PINNA
urls.py

Created by Shota Shimazu on 2018/03/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.urls import path
from paydo.views import """YOUR_VIEW_CLASSIES"""

urlpatterns = [
    path(r'^url_letter/', """YOUR_VIEW_CLASS""".as_view(), name='starts'),
]
