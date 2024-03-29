"""
PINNA Serveur
temporary.py

Created by Shota Shimazu on 2018/2/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import tempfile
import contextlib
import uuid
import os

from . import fileable


@contextlib.contextmanager
def tmpWorking(tmp_name):

    # Directories
    working = tmp_name + uuid.uuid4()
    current = os.getcwd()
    
    # Enter
    fileable.mkdir(working)
    os.chdir(working)
    yield

    # Exit
    os.chdir(current)
    fileable.rm(working)



class FileableTemporary():
    """
    [WIP] Fileable Advanced Temporary Working Space
    """

    def __init__(self, name):
        self._tmp_name = name
        self._tmp_dir  = os.getcwd() + self._tmp_name + uuid.uuid4()

    def getTempDirectory(self):
        return self._tmp_name
