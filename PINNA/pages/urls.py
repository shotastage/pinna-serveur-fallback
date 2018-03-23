"""
PINNA
urls.py

Created by Shota Shimazu on 2018/03/01

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.urls import path
from pages.views import Landings

urlpatterns = [
    path('', Landings.as_view(), name='landing'),
]
