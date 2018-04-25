"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/15

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.db import models
from django.utils import timezone
from secrets import token_urlsafe, token_hex



class PubulishedLicense(models.Model):
  key           = models.CharField(max_length = 255)
  license_name  = models.CharField(max_length = 255)
  product       = models.CharField(max_length = 255)
  created_at    = models.DateTimeField(default = timezone.now)
  is_activated  = models.BooleanField(default = False)

  def publish_key(self):
    self.key = token_urlsafe(16)
    return self.key


class RevokedLicense(models.Model):
  key         = models.CharField(max_length = 255)
  revoked_at  = models.DateTimeField(default = timezone.now)
  reason      = models.CharField(max_length = 255, blank = True)
