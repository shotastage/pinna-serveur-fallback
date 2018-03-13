"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.db import models

# Create your models here.


class Pinner(models.Model):
  user_id   = models.UUIDField()
  current   = models.CharField(max_length = 255)
  status    = models.CharField(max_length = 255)
