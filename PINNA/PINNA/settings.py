"""
PINNA
settings.py

Created by Shota Shimazu on 2018/02/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os
from .environment import production
from .environment import development
from .environment import ci


try:
    MODE = os.environ["PINNA_RUNNING_MODE"]
except:
    MODE = "devel"


if MODE == "devel":
    settings = development
elif MODE == "ci":
    settings = ci
else:
    settings = production


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = settings.BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = settings.DEBUG

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = settings.DEBUG

ALLOWED_HOSTS = settings.ALLOWED_HOSTS



# Application definition

INSTALLED_APPS = settings.INSTALLED_APPS

MIDDLEWARE = settings.MIDDLEWARE

ROOT_URLCONF = settings.ROOT_URLCONF

TEMPLATES = settings.TEMPLATES

WSGI_APPLICATION = settings.WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = settings.DATABASES

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = settings.AUTH_PASSWORD_VALIDATORS


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = settings.LANGUAGE_CODE

TIME_ZONE = settings.TIME_ZONE

USE_I18N = settings.USE_I18N

USE_L10N = settings.USE_L10N

USE_TZ = settings.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = settings.STATIC_URL
