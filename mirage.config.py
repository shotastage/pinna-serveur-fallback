"""
PINNA
mirage.config.py

Created by Shota Shimazu on 2018/03/19

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from mirage import system as mys
from mirage.confscript import ConfigScript


MIRAGE_CONFIG_SCRIPT_VERSION = "0.0.1"
MIRAGE_CONFIG_DEFAULT_CLASS = "MirageConfig"


class MirageConfig(ConfigScript):
    
    def initialize(self) -> None:
        mys.log("PINNA Setting Script V0.0.1")

    
    def main():
        self.register_custom_command("raml-ide", None, "tools/scripts/mirage_raml.py")



    def deinitialize(self) -> None:
        mys.log("Bye : )")
