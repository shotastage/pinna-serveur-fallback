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
from secrets import token_urlsafe, compare_digest
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
  credential    = models.CharField(max_length = 255, default = token_urlsafe(64))
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


class PendingRegistration(models.Model):
  """
  email                 New registration email address
  created_on            Date & time of registering on pending
  verification_code     URL-safe token to verificate a registration
  is_revoked            Boolean value whether the verification code is revoked or not
  """

  email             = models.EmailField()
  created_on        = models.DateTimeField(default = timezone.now)
  verification_code = models.CharField(max_length = 255, default = token_urlsafe(64))
  is_revoked        = models.BooleanField(default = False)



class OneTapLogin(models.Model):
  """
  token                 URL-safe token to verificate a one tap tapping!
  is_tapped             Boolean value whether the "one tap" is tapped or not
  is_revoked            Boolean value whether the verification code is revoked or not
  created_on            Date & time of one tap session
  """
  
  token       = models.CharField(max_length = 255, default = token_urlsafe(64))
  is_tapped   = models.BooleanField(default = False)
  is_revoked  = models.BooleanField(default = False)
  created_on  = models.DateTimeField(default = timezone.now)
