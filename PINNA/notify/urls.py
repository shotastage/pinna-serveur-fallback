"""
PINNA
apns.py

Created by Shota Shimazu on 2018/02/19

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.urls import path
from notify.views import """YOUR_VIEW_CLASSIES"""

urlpatterns = [
    path(r'^url_letter/', """YOUR_VIEW_CLASS""".as_view(), name='starts'),
]