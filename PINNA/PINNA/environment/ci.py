"""
PINNA
ci.py

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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
        },
    }
}

""" backup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pinna_gitlab_ci',
        'USER': 'gitlab_ci',
        'PASSWORD': 'test_passwd_for_ci',
        'HOST': 'postgres',
        'PORT': 5432,
        'TEST': {
            'NAME': 'pinna_gitlab_ci_testing',
        },
    }
}
"""
