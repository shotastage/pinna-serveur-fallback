"""
PINNA
sender.py

Created by Shota Shimazu on 2018/03/13

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://git.mixstage.tokyo/Piu/piu-serveur/blob/master/LICENSE
"""

from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from uuid import uuid4
from enum import Enum
from .models import SentMail



class ArtilleryMail():
    """
    Mail Creation Class which is only for a single sending target

    Init:
        - to_email          Email To
        - from_email        From email
        - reply_email       Reply email
        - subject           Mail subject
        - template          Template path
        - mail_id           Mail ID ( UUID )
    """

    def __init__(self, to_email: str, from_email: str,
                 reply_email: str, subject: str, html: str, text: str, mail_id = None):
        self._to, self._from, self._reply      = to_email, from_email, reply_email
        self._subject, self._html, self._text  = subject, html, text
        self._id     = mail_id
        self._result = ShootResult.succeeded

        if self._id is None: self._id = uuid4()


    def send(self) -> None:
        """
        Send E-mail using Django mail backend & register E-mail contents to database.
        """
        mail = EmailMultiAlternatives(
            subject     = self._subject,
            body        = self._text,
            from_email  = self._from,
            to          = [self._to],
            bcc         = [],
            reply_to    = [self._reply],
            headers     = {'Message-ID': self._id},
        )

        # Attach HTML contents
        if not self._html is None:
            mail.attach_alternative(self._html, "text/html")
            contents_type = 1
        else:
            contents_type = 0

        # Send email
        mail.send(fail_silently = False)

        # Create Mail Log
        maillog = SentMail(
            subject         = self._subject,
            body            = self._text,
            contents_type   = contents_type,
            from_email      = self._from,
            to              = self._to,
            reply_to        = self._reply,
            mailid          = self._id,
        )

        # Save mail log
        maillog.save()

        return (self._id, self._result)


    @staticmethod
    def renderHTML(template, context = None) -> str:
        return render_to_string(template, context)



class ArtilleryMassMails(ArtilleryMail):
    """
    Mail Creation Class which is only for a single sending target

    Init:
        - to_emails         Email To
        - from_email        From email
        - reply_email       Reply email
        - subject           Mail subject
        - template          Template path
        - mail_id           Mail ID ( UUID )
    """

    def __init__(self, to_emails: list, from_email: str,
                 reply_email: str, subject: str, html: str, text: str, mail_id = None):
        self._to, self._from, self._reply = to_emails, from_email, reply_email
        self._subject, self._html, self._text = subject, html, text
        self._id = mail_id
        self._result = ShootResult.succeeded

        if self._id is None: self._id = uuid4()


    def send(self) -> None:
        """
        Send E-mail using Django mail backend & register E-mail contents to database.
        """
        mail = EmailMultiAlternatives(
            subject     = self._subject,
            body        = self._text,
            from_email  = self._from,
            to          = [self._reply],
            bcc         = self._to,
            reply_to    = [self._reply],
            headers     = {'Message-ID': self._id},
        )

        # Attach HTML contents
        if not self._html is None:
            mail.attach_alternative(self._html, "text/html")
            contents_type = 1
        else:
            contents_type = 0

        # Send email
        mail.send(fail_silently = False)

        # Create Mail Log
        maillog = SentMail(
            subject         = self._subject,
            body            = self._text,
            contents_type   = contents_type,
            from_email      = self._from,
            to              = self._to,
            reply_to        = self._reply,
            mailid          = self._id,
        )

        # Save mail log
        maillog.save()

        return (self._id, self._result)



class ShootResult(Enum):
    succeeded = 0
    failed = 1
