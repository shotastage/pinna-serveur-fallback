"""
PINNA
models.py

Created by Shota Shimazu on 2018/02/24

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.db import models

# Create your models here.


class User(models.Model):
  user_name = models.CharField(max_length = 255)
  email     = models.EmailField()


class UserProfile(User):
  first_name  = models.CharField(max_length = 255)
  last_name   = models.CharField(max_length = 255)
  middle_name = models.CharField(max_length = 255)
  gender      = models.IntegerField()
  age         = models.IntegerField()
  country     = models.CharField(max_length = 255)
  phone       = models.CharField(max_length = 255)
  address     = models.CharField(max_length = 255)
