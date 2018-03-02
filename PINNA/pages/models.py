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
  domain        = models.CharField(max_length = 255, default = "ServingPage")
  sub_path      = models.CharField(max_length = 255)
  parent        = models.UUIDField(null = True)
  published     = models.BooleanField(default = False)
  date          = models.DateTimeField()
  created_by    = models.CharField(max_length = 255)
  publishing_limitation = models.CharField(max_length = 255, default = "internal")


  def __str__(self):
    return self.site_id


  def get_template_path(self):
    return self.template_path


class SimpleTextPages(ServingPages):
  title = models.CharField(max_length = 255)
  subtitle = models.CharField(max_length = 255)
  contents = models.TextField()


class RichContentsPages(ServingPages):
  title = models.CharField(max_length = 255)
  subtitle = models.CharField(max_length = 255)


class LandingPage(RichContentsPages):
  is_landing = models.BooleanField()


class LicensePage(ServingPages):
  is_serving = models.BooleanField()


class HelpPages(ServingPages):
  # Help page version
  version               = models.CharField(max_length = 255)

  # Help page category or title to find out from help database
  help_indentification  = models.CharField(max_length = 255)

  # Filed for questionare to ask this help page usefull or unusefull
  usefull               = models.IntegerField()
  unusefull             = models.IntegerField()

  # Files for saving is user need another detail help page
  need_another_help = models.BooleanField()
