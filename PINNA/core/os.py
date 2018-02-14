"""
PINNA Serveur
os.py

Created by Shota Shimazu on 2018/2/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os
import contextlib


@contextlib.contextmanager
def onDir(path):
    current = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current)
