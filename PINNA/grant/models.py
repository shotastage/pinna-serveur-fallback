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
import secrets


class DeviceCredential(models.Model):
  """
  Models docstring is here.
  """
  id          = models.UUIDField(primary_key = True, default = uuid4)
  credential  = models.CharField(max_length = 255)
  name        = models.CharField(max_length = 255)
  os          = models.CharField(max_length = 255)

  def create(self):
    pass


  def publish_credential(self):
    return secrets.token_hex()

  def certificate(self, credential):
    return secrets.compare_digest(credential, self.credential)



class PendingRegistration(models.Model):
  is_valid_email  = models.EmailField()
  created_on      = models.DateTimeField(default = timezone.now)
  is_invoked      = models.BooleanField(default = False)



class OneTapLogin(models.Model):
  mail_token  = models.UUIDField(default = uuid4)
  is_tapped   = models.BooleanField(default = False)
  is_invoked  = models.BooleanField(default = False)
  created_on  = models.DateTimeField(default = timezone.now)
