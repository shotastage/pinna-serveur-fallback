"""
PINNA
Miragefile.py

Created by Shota Shimazu on 2018/03/19

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from mirage.core import Void
from mirage import system as mys
from mirage.confscript import ConfigScript
from mirage.confscript.settings import Settings


MIRAGE_CONFIG_SCRIPT_VERSION = "0.0.1"
MIRAGE_CONFIG_DEFAULT_CLASS = "MirageConfig"


class MirageConfig(ConfigScript):

    BASIC_PROJECT = {
        "NAME": "PINNA",
        "VERSION": "0.0.1",
        "AUTHOR": "Shota Shimazu <hornet.live.mf@gmail.com>",
        "GIT_URL": "git@hplab.work:pinna-music/pinna-music.git",
        "LICENSE": Settings.License.original,
        "DESCRIPTION": "MUSIC ON THE MAP!",
    }

    DJANGO_PROJECT = {
        "path": "PINNA",
        "module": "PINNA",
        "package": "pipenv",
        "database": "PostgreSQL",
    }

    FRONT_END_PROJECT = {
        "path": "shell",
        "package": "yarn",
        "builder": "webpack",
    }

    COPYRIGHT = {
        "start_year": 2018,
        "copyrightors": [
            "Shota Shimazu"
        ]
    }



    def initialize(self) -> Void:
        mys.log("PINNA Setting Script V0.0.1")


    def main(self) -> int:
        self.register_custom_command("raml-ide", None, "tools/scripts/mirage_raml.py")
        self.register_custom_command_with_runtime("clean:mac", "tools/setup/clean-mac.rb", "ruby")

        return 0


    def deinitialize(self) -> Void:
        mys.log("Bye : )")
