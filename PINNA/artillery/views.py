"""
PINNA
views.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.shortcuts import render, redirect
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
        
        context = { "mail_result": "Not sent" }

        return render(request, 'DebugSendTemplate.html', context)


    @debug
    def post(self, request):

        result = "Succeeded"

        html_contents = ArtilleryMail.renderHTML(
            template    = "TestHTMLMail.html",
            context     = { "message": request.POST["message"] }
        )

        mail = ArtilleryMail(
            to_email    = request.POST["mail_to"],        # To
            from_email  = "Artillery Mail Sender <web_devel@labbiness.com>", # From
            reply_email = "web_devel@labbiness.com",      # Reply address
            subject     = request.POST["subject"],        # Email Subject
            html        = html_contents,                  # Email View Template
            text        = request.POST["message"],        # Email Body
        )

        mail.send()
    

        context = { "mail_result": result }

        return render(request, 'DebugSendTemplate.html', context)
