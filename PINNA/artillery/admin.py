"""
PINNA
admin.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.contrib import admin
from .models import PendingMail, SentMail

admin.site.register(PendingMail)
admin.site.register(SentMail)
