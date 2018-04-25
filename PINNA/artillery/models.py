"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from uuid import uuid4


class PendingMail(models.Model):
  mailid      = models.UUIDField(default = uuid4)
  to_users    = ArrayField(models.CharField(max_length = 255), size=1000)
  from_user   = models.CharField(max_length = 255)
  subject     = models.CharField(max_length = 255)
  text        = models.TextField()
  created_at  = models.DateTimeField(default = timezone.now)
  send_schedule = models.DateTimeField(default = timezone.now)
  is_sent     = models.BooleanField(default = False)



class SentMail(models.Model):
  
  CONTENTS_TYPE = (
    (0, 'text/plain'),
    (1, 'text/html'),
  )

  SEND_RESULT = (
    (0, 'success'),
    (1, 'fail')
  )

  subject         = models.CharField(max_length = 255)
  body            = models.TextField()
  contents_type   = models.IntegerField(default = 0, choices = CONTENTS_TYPE)
  disp_name       = models.CharField(max_length = 255, blank = True)
  from_email      = models.EmailField()
  to              = models.CharField(max_length = 1000)
  bcc             = models.CharField(max_length = 1000, blank = True)
  reply_to        = models.CharField(max_length = 255)
  headers         = models.CharField(max_length = 255, blank = True)

  mailid          = models.UUIDField(default = uuid4)
  created_on      = models.DateTimeField(default = timezone.now)
  result          = models.IntegerField(default = 0, choices = SEND_RESULT)
