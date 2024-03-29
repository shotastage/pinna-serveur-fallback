"""
PINNA
admin.py

Created by Shota Shimazu on 2018/03/01

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.contrib import admin

# Register your models here.
from .models import ServingPages, SimpleTextPages, RichContentsPages, LandingPage, LicensePage, HelpPages

admin.site.register(ServingPages)
admin.site.register(SimpleTextPages)
admin.site.register(RichContentsPages)
admin.site.register(LandingPage)
admin.site.register(LicensePage)
admin.site.register(HelpPages)
