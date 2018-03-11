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
from uuid import uuid4


class PendingMail(models.Model):
  mailid      = models.UUIDField(default = uuid4)
  to_users    = ArrayField(models.CharField(max_length = 255), size=1000)
  from_user   = models.CharField(max_length = 255)
  title       = models.CharField(max_length = 255)
  body        = models.TextField()
  created_on  = models.DateTimeField()
  is_sent     = models.BooleanField()


class SentMail(models.Model):
  mailid      = models.UUIDField(default = uuid4)
  to_users    = ArrayField(models.CharField(max_length = 255), size=1000)
  from_user   = models.CharField(max_length = 255)
  title       = models.CharField(max_length = 255)
  body        = models.TextField()
  created_on  = models.DateTimeField()
