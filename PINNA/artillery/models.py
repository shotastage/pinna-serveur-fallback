"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
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
  mailid      = models.UUIDField(default = uuid4)
  to_users    = ArrayField(models.CharField(max_length = 255), size=1000)
  from_user   = models.CharField(max_length = 255)
  title       = models.CharField(max_length = 255)
  body        = models.TextField()
  created_on  = models.DateTimeField()
