"""
PINNA
models.py

Created by Shota Shimazu on 2018/03/01

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.db import models



class ServingPages(models.Model):
  site_id       = models.UUIDField(primary_key = True)
  template_path = models.FilePathField()
  domain        = models.CharField(max_length = 255)
  sub_path      = models.CharField(max_length = 255)
  parent        = models.UUIDField()
  published     = models.BooleanField()
  date          = models.DateTimeField()


class LandingPage(ServingPages):
  title: models.CharField(max_length = 255)


class DocumentPage(ServingPages):
  version       = models.CharField(max_length = 255)
  document_type = models.CharField(max_length = 255)
