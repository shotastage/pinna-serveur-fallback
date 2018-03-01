"""
PINNA
settings.py

Created by Shota Shimazu on 2018/02/22

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import os, sys
from pathlib import Path, PurePath
from .environment.base import *


try:
    RUNNING_MODE = os.environ["PINNA_RUNNING_MODE"]
except:
    RUNNING_MODE = "devel"


if RUNNING_MODE == "prod":
    try:
        print("Using production...")
        from .environment.production import *
    except ImportError:
        pass

elif RUNNING_MODE == "devel":
    try:
        print("Using development...")
        from .environment.development import *
    except ImportError:
        pass

elif RUNNING_MODE == "ci":
    try:
        print("Using ci...")
        from .environment.ci import *
    except ImportError:
        pass

else:
    try:
        print("Using development...")
        from .environment.production import *
    except ImportError:
        pass
