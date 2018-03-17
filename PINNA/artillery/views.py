"""
PINNA
views.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.shortcuts import render
from django.conf import settings
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from core.functional import debug
from .sender import ArtilleryMail, ArtilleryMassMails



class MailSendView(APIView):
    
    def post(self, request):
        pass

    def get(self, request):
        pass


class DebugMailSendView(View):
    
    @debug
    def get(self, request):
        
        context = {
            "smtp_host": settings.EMAIL_HOST,
            "smtp_port": settings.EMAIL_PORT,
            "smtp_user": settings.EMAIL_HOST_USER,
            "mail_result": "Not sent",
        }

        return render(request, 'DebugSendTemplate.html', context)


    @debug
    def post(self, request):

        result = "Succeeded"

        mail = ArtilleryMail(
            request.POST["mail_to"],         # To
            "Artillery Mail Sender <web_devel@labbiness.com>",       # From
            "web_devel@labbiness.com",       # Reply address
            request.POST["subject"],         # Email Subject
            request.POST["message"],         # Email View Template
        )

        mail.send()
    

        context = {
            "smtp_host": settings.EMAIL_HOST,
            "smtp_port": settings.EMAIL_PORT,
            "smtp_user": settings.EMAIL_HOST_USER,
            "mail_result": result,
        }

        return render(request, 'DebugSendTemplate.html', context)
