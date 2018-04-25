"""
PINNA
urls.py

Created by Shota Shimazu on 2018/03/16

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.urls import path
from pvs.views import """YOUR_VIEW_CLASSIES"""

urlpatterns = [
    path('url_letter/', """YOUR_VIEW_CLASS""".as_view(), name='starts'),
]
