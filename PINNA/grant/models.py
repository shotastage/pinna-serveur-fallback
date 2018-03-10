"""
PINNA
models.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.db import models
from django.utils import timezone
from uuid import uuid4
from secrets import token_hex, compare_digest


class DeviceCredential(models.Model):
  """
  Models docstring is here.
  """
  id          = models.UUIDField(primary_key = True, default = uuid4)
  credential  = models.CharField(max_length = 255, default = token_hex(32))
  device_name = models.CharField(max_length = 255)
  device_token = models.UUIDField(default = uuid4)
  useragent = models.CharField(max_length = 255)
  is_revoked = models.BooleanField(default = False)


  def create(self):
    self.credential = token_hex(32)

  def update(self):
    self.create()

  def certificate(self, credential):
    return compare_digest(credential, self.credential)

  def revoke(self):
    self.is_revoked = True


class PendingRegistration(models.Model):
  is_valid_email  = models.EmailField()
  created_on      = models.DateTimeField(default = timezone.now)
  is_revoked      = models.BooleanField(default = False)



class OneTapLogin(models.Model):
  mail_token  = models.UUIDField(default = uuid4)
  is_tapped   = models.BooleanField(default = False)
  is_revoked  = models.BooleanField(default = False)
  created_on  = models.DateTimeField(default = timezone.now)
