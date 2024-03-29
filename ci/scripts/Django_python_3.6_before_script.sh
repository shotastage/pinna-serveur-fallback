#!/usr/bin/env sh
#
# PINNA
# Django_python_3.6_before_script.sh
#
# Created by Shota Shimazu on 2018/03/13
#
# Copyright (c) 2018 Shota Shimazu All Rights Reserved.
#
# This software is released under the terms of restricted, see LICENSE for detail.
# https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
#

apt-get update -qq && apt-get install -y -qq postgresql postgresql-contrib libpq-dev cmake
pip install --upgrade pip
pip install -r ./requirements/locked.txt
pip install django-mirage
