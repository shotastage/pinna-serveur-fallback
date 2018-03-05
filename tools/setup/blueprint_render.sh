#!/usr/bin/env bash
# PINNA
# install_blueprint_render.sh
#
# Created by Shota Shimazu on 2018/03/05
#
# Copyright (c) 2018 Shota Shimazu All Rights Reserved.
#
# This software is released under the terms of restricted, see LICENSE for detail.
# https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE


function on_mac_os
{
    brew tap bukalapak/packages
    brew install snowboard
}

function on_linux
{
    echo "Downloading snowboard..."
    git clone https://github.com/bukalapak/snowboard.git
    cd snowboard
    make install
}
