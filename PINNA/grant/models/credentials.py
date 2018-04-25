"""
PINNA
credentials.py

Created by Shota Shimazu on 2018/03/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from secrets import token_urlsafe, compare_digest, token_hex
from uuid import uuid4


class DeviceCredential(models.Model):
  """
  ID                    device unique UUID
  credential            URL-safe 64 bit token
  device_name           Device name (e.g, SHOTA's iPhone7)
  useragent             Useragent like browser (e.g. Macintosh; Intel Mac OS X 10_13_3 Web/3.1)
  is_revoked            Boolean value whether the token is revoked or not
  """

  id            = models.UUIDField(primary_key = True, default = uuid4)
  credential    = models.CharField(max_length = 255)
  device_name   = models.CharField(max_length = 255)
  useragent     = models.CharField(max_length = 255)
  is_revoked    = models.BooleanField(default = False)


  def create(self):
    self.credential = token_hex(32)

  def update(self):
    self.create()

  def certificate(self, credential):
    return compare_digest(credential, self.credential)

  def revoke(self):
    self.is_revoked = True
