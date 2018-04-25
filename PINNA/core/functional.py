"""
PINNA
functional.py

Created by Shota Shimazu on 2018/03/17

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

import functools
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import status



def allow(setting):
    """
    Decorator for forbid to access without permission of setting.
    """

    def _allow(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if setting:
                return func(*args,**kwargs)
            else:
                return Response(status = status.HTTP_404_NOT_FOUND)
        return wrapper


def debug(func):
    """
    Decorator for forbid to access without debugging.
    """

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if settings.DEBUG:
            return func(*args,**kwargs)
        else:
            return Response(status = status.HTTP_404_NOT_FOUND)
    return wrapper
