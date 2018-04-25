"""
PINNA
lazyusers.py

Created by Shota Shimazu on 2018/03/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from secrets import token_urlsafe, compare_digest
from uuid import uuid4
