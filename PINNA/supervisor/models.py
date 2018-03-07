"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.db import models

# Create your models here.


class AdminTheme(models.Model):
  prod_title  = models.CharField(max_length = 255)
  logo        = models.CharField(max_length = 255)
