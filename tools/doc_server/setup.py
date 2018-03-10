"""
PINNA
setup.py

Created by Shota Shimazu on 2018/03/09

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

import os
import contextlib



@contextlib.contextmanager
def InDir(path):
    current = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current)


def execute(*cmds):
    for cmd in cmds:
        os.system(cmd)


def build_apib():
    
    with InDir("../../"):
        execute(
            "rm -rf ./tools/doc_server/templates/api.html",
	        "mkdir api_site"
	        "snowboard html -o ./api_site/index.html ./blueprints/v1.apib",
	        "mv ./api_site/index.html ./tools/doc_server/templates/api.html",
	        "rm -rf api_site",
        )
