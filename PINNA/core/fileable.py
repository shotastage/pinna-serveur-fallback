"""
PINNA Serveur
os.py

Created by Shota Shimazu on 2018/2/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os
import shutil


def exists(path):
    return os.path.exists(path)


def copy(from_path, to_path, force = False):
    if os.path.exists(to_path):
        if force:
            shutil.rmtree(to_path)
        else:
            raise FileExistsError
            return
    
    shutil.copytree(from_path, to_path)


def move(from_path, to_path, force = False):
    shutil.move(from_path, to_path)


def mkdir(path):
    os.makedirs(path)


def rm(path):
    shutil.rmtree(path)


def cwd():
    return os.getcwd()


def cd(path):
    os.chdir(path)
