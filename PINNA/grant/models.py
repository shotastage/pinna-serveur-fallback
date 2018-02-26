"""
PINNA
models.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.db import models
import secrets


class DeviceCredential(models.Model):
  """
  Models docstring is here.
  """
  id          = models.UUIDField(primary_key = True)
  credential  = models.CharField(max_length = 255)
  device      = models.CharField(max_length = 255)
  os          = models.CharField(max_length = 255)


  def public_credential(self):
    return secrets.token_hex()

  def certificate(self, credential):
    return secrets.compare_digest(credential, self.credential)
