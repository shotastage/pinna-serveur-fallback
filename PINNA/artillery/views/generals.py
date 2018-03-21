"""
PINNA
generals.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.views import View
from django.utils.functional import cached_property
from rest_framework.views import APIView
from rest_framework.response import Response
from core.functional import debug
from ..sender import ArtilleryMail, ArtilleryMassMails



class MailSendView(APIView):
    
    def post(self, request):
        pass

    def get(self, request):
        pass
