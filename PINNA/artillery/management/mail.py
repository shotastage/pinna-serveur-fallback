"""
PINNA
mail.py

Created by Shota Shimazu on 2018/03/13

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

import time
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from artillery.models import PendingMail
