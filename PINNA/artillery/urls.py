"""
PINNA
tests.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.urls import path
from artillery.views import MailSendView, DebugMailSendView


urlpatterns = [
    path('sendmail', MailSendView.as_view(), name='starts'),
    path('sendmail/ondebug/', DebugMailSendView.as_view()),
]
