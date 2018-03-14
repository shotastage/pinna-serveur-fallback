"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/15

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.db import models

# Create your models here.


class PubulishedLicense(models.Model):
  key           = models.CharField(max_length = 255)
  license_name  = models.CharField(max_length = 255)
  product       = models.CharField(max_length = 255)
  created_at    = models.DateTimeField()
