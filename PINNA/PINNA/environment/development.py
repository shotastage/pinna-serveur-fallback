"""
PINNA
development.py

Created by Shota Shimazu on 2018/02/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbp90ec1v51e12',
        'USER': 'frvselsvkmqtbm',
        'PASSWORD': '4712ce5560eba837a35b4d1e755a352b706e6b41d32fa8fa2a3f0a66eeec9599',
        'HOST': 'ec2-107-22-236-252.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
