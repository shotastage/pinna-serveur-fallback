"""
PINNA
development.py

Created by Shota Shimazu on 2018/02/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os
import getpass
from .common import *


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pinna_devel',
        'USER': getpass.getuser(),
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
        'TEST': {
            'NAME': 'pinna_test',
        },
    }
}


# Cache
# https://docs.djangoproject.com/en/2.0/ref/settings/#caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# Django Email Settings
# https://docs.djangoproject.com/en/2.0/topics/email/#obtaining-an-instance-of-an-email-backend

EMAIL_HOST = 'smtp.happinesslab.conoha.io'
EMAIL_PORT = 587
EMAIL_HOST_USER = "web_devel@labbiness.com"
EMAIL_HOST_PASSWORD = "z7rA62zDrKyqxrBpvfjQyg"
EMAIL_USE_TLS = True
