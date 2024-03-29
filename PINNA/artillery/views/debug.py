"""
Piu
debug.py

Created by Shota Shimazu on 2018/03/22

Copyright (c) 2018 MiXSTAGE, Inc All Rights Reserved.
Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA & Piu Cloud System License, see LICENSE for detail.
https://git.mixstage.tokyo/Piu/piu-serveur/blob/master/LICENSE
"""

from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.views import View
from django.utils.functional import cached_property
from rest_framework.views import APIView
from rest_framework.response import Response
from core.functional import debug
from ..sender import ArtilleryMail, ArtilleryMassMails



class DebugMailSendView(View):

    @debug
    def get(self, request) -> HttpResponse:

        context = { "mail_result": "Not sent" }

        return render(request, 'DebugSendTemplate.html', context)


    @debug
    def post(self, request) -> HttpResponse:

        result = "Succeeded"

        html_contents = ArtilleryMail.renderHTML(
            template    = "TestHTMLMail.html",
            context     = { "message": request.POST["message"] }
        )

        mail = ArtilleryMail(
            to_email    = request.POST["mail_to"],
            from_email  = settings.ARTILLERY_SENDER_DEBUG,
            reply_email = settings.ARTILLERY_SENDER_REPLY_DEBUG,
            subject     = request.POST["subject"],
            html        = html_contents,                  # Email View Template
            text        = request.POST["message"],        # Email Body
        )

        mail.send()


        context = { "mail_result": result }

        return render(request, 'DebugSendTemplate.html', context)
