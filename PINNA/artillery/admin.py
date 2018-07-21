"""
Piu
admin.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://git.mixstage.tokyo/Piu/piu-serveur/blob/master/LICENSE
"""

from django.contrib import admin
from .models import PendingMail, SentMail


class SentMailAdmin(admin.ModelAdmin):
    readonly_fields = (
        "subject",
        "body",
        "contents_type",
        "disp_name",
        "from_email",
        "to",
        "bcc",
        "reply_to",
        "headers",
        "created_on",
        "result",
    )


admin.site.register(SentMail, SentMailAdmin)
admin.site.register(PendingMail)
