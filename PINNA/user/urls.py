"""
PINNA
urls.py

Created by Shota Shimazu on 2018/02/24

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.conf.urls import url
from user.views import """YOUR_VIEW_CLASSIES"""

urlpatterns = [
    url(r'^url_letter/', """YOUR_VIEW_CLASS""".as_view(), name='starts'),
]