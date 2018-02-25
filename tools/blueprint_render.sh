#!/usr/bin/env bash


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
