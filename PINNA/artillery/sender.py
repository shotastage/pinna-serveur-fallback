"""
PINNA
sender.py

Created by Shota Shimazu on 2018/03/13

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives, send_mail




class ArtilleryMail():

    def __init__(self, to_address, from_address, subject, text):
        self._to = to_address
        self._from = from_address
        self._subject = subject
        self._text = text


    def send(self):
        send_mail(
            self._subject,
            self._text,
            self._from,
            self._to,
            fail_silently = False,
        )
