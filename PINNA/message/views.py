"""
PINNA Serveur
views.py

Created by Shota Shimazu on 2018/2/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of StreetStory Software License, see LICENSE for detail.
https://hplab.work/StreetStory/streetstory-serveur/blob/master/LICENSE
"""

import random
import string
from django.db import transaction
from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class ManageChatroomVue(APIView):
    """
    API View to create or destory chat room.

    * Only authenticated users can access this routing.
    """
