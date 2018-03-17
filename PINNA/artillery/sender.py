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
from enum import Enum
from .models import SentMail



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
        self._to, self._from, self._reply = to_email, from_email, reply_email
        self._subject = subject
        self._template = template
        self._id = mail_id
        self._result = ArtilleryShootResult.succeeded

        if self._id is None: self._id = uuid4()


    def send(self):

        email = EmailMessage(
            subject     = self._subject,
            body        = self._template,
            from_email  = self._from,
            to          = [self._to],
            bcc         = [],
            reply_to    = [self._reply],
            headers     = {'Message-ID': self._id},
        )

        
        email.send(fail_silently = False)
        

        maillog = SentMail(
            subject = self._subject,
            body = self._template,
            contents_type = 0,
            from_email = self._from,
            to = self._to,
            reply_to = self._reply,
            mailid = self._id,
        )

        maillog.save()

        return (self._id, self._result)



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
        self._to, self._from, self._reply = to_emails, from_email, reply_email
        self._subject = subject
        self._template = template
        self._id = mail_id
        self._result = ArtilleryShootResult.succeeded

        if self._id is None: self._id = uuid4()        


    def send(self):

        email = EmailMessage(
            subject     = self._subject,
            body        = self._template,
            from_email  = self._from,
            to          = [self._reply],    # Reply address instead of To addresses
            bcc         = [self._to],       # To addresses instead of BCC
            reply_to    = [self._reply],
            headers     = {'Message-ID': self._id},
        )

        email.send(fail_silently = False)

        return (self._id, self._result)


class ArtilleryShootResult(Enum):
    succeeded = 0
    failed = 1
