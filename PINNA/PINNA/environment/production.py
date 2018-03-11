"""
PINNA
production.py

Created by Shota Shimazu on 2018/02/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["PINNA_SECRET_KEY"]

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pinna_production',
        'USER': 'pinna_production_user',
        'PASSWORD': 'secret_password',
        'HOST': 'localhost',
        'PORT': 5432,
        'TEST': {
            'NAME': 'pinna_test',
        },
    }
}
