#!/usr/bin/env sh
#
# PINNA
# Validation_ubuntu_python_script.sh
#
# Created by Shota Shimazu on 2018/03/13
#
# Copyright (c) 2018 Shota Shimazu All Rights Reserved.
#
# This software is released under the terms of restricted, see LICENSE for detail.
# https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
#

pyenv install 3.6.4
pyenv global 3.6.4
pip install pipenv
pipenv --three
pipenv install
pipenv install --dev
pipenv run mg v
