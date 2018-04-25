"""
PINNA
asgi.py

Created by Shota Shimazu on 2018/03/12

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""


import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multichat.settings")

django.setup()
application = get_default_application()
