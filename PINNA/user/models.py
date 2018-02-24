"""
PINNA
models.py

Created by Shota Shimazu on 2018/02/24

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.db import models

# Create your models here.


class User(models.Model):
  user_name = models.CharField()
  email     = models.CharField()


class UserProfile(User):
  first_name  = models.CharField()
  last_name   = models.CharField()
  middle_name = models.CharField()
  gender      = models.IntegerField()
  age         = models.IntegerField()
  country     = models.CharField()
  phone       = models.CharField()
  address     = models.CharField()
