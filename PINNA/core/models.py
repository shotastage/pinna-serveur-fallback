"""
PINNA Serveur
models.py

Created by Shota Shimazu on 2018/2/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.db import models
from django.utils import timezone
from uuid import uuid4


class OptimizationSchedule(models.Model):
  scheduled_by      = models.CharField(max_length = 255)
  optimization_id   = models.UUIDField(default = uuid4)
  influencer        = models.CharField(max_length = 255)
  finished          = models.BooleanField(default = False)
  start_at          = models.DateTimeField(default = timezone.now)
