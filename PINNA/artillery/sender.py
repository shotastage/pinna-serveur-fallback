"""
PINNA
sender.py

Created by Shota Shimazu on 2018/03/13

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from uuid import uuid4



class ArtilleryMail():
    """
    Mail Creation Class which is only for a single sending target

    Init:
        - to_email          Email TO
        - from_email        From email
        - reply_email       Reply email
        - subject           Mail subject
        - template          Template path
        - mail_id           Mail ID ( UUID )
    """

    def __init__(self, to_email, from_email, reply_email, subject, template, mail_id = None):
        self._to = to_email
        self._from = from_email
        self._reply = reply_email
        self._subject = subject
        self._template = template

        if mail_id is None:
            self._id = uuid4()
        else:    
            self._id = mail_id


    def send(self):

        email = EmailMessage(
            self._subject,
            self._template,
            self._from,
            [self._to],
            [], # BCC Emails
            [self._reply],
            headers={'Message-ID': 'foo'},
        )


class ArtilleryMassMails():
    """
    Mail Creation Class which is only for a single sending target

    Init:
        - to_emails         Email TO
        - from_email        From email
        - reply_email       Reply email
        - subject           Mail subject
        - template          Template path
        - mail_id           Mail ID ( UUID )
    """
    
    def __init__(self, to_emails, from_email, reply_email, subject, template, mail_id = None):
        self._to = to_emails
        self._from = from_email
        self._reply = reply_email
        self._subject = subject
        self._template = template
        if mail_id is None:
            self._id = uuid4()
        else:    
            self._id = mail_id


    def send(self):

        email = EmailMessage(
            self._subject,
            self._template,
            self._from,
            [self._reply], # Reply address instead of To addresses
            [self._to],  # To addresses instead of BCC
            [self._reply],
            headers={'Message-ID': 'foo'},
        )
