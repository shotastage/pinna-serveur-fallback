#!/usr/bin/env ruby

"""
PINNA
setup_mac.rb

Created by Shota Shimazu on 2018/03/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

require 'rbconfig'


def is_macos
    @os ||= (
        host_os = RbConfig::CONFIG['host_os']
        case host_os
        when /darwin|mac os/
            return true
        else
            return false
        end
    )
end

def homebrew
    system("brew update")
    system("brew upgrade")
end

def install_packages
    system("brew install pyenv redis node yarn")
end

def install_python
    system("pyenv install 3.6.4")
    system("pyenv global 3.6.4")
    system("pip install pipenv")
end

def main
    puts "PINNA Devel Setup for macOS"
    
    if is_macos
        puts "Platform: OK 👍"
    else
        puts "This script is only for macOS!"
        return
    end

    puts "Upgrading all brew packages..."
    homebrew

    puts "Installing requires packages..."
    install_packages
    install_python
end

main
