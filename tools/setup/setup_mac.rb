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


def initializations
    ARGV.each_with_index do |arg, i|
        puts "ARGV[#{i}]：#{arg}"
    end
end


class HomebrewRelated

    is_failed = true

    def initialize
        puts "Upgrading all homebrew package..."
        homebrew
        puts "Installing required packages..."
        install_packages
    end

    def homebrew
        system("brew update")
        system("brew upgrade")
    end

    def install_packages
        system("brew install pyenv redis node yarn")
        system("brew tap bukalapak/packages")
        system("brew install snowboard")
    end
end


class PyenvRelated

    is_failed = true

    def initialize
        @instllation = false

        check
        install
    end

    def check
        global = `pyenv global`
        if global.include?("3.6.4") then
            puts "Required Python is already installed."
            @instllation = true
        end
    end

    def install

        unless @instllation then
            puts "Installing required python..."
            system("pyenv install 3.6.4")
            system("pyenv global 3.6.4")
            system("pip install pipenv")
        end
    end
end


def main

    puts "PINNA Devel Setup for macOS"

    # Check platform
    if is_macos
        puts "Platform: OK 👍"
    else
        puts "This script is only for macOS!"
        return
    end

    # Initial functions
    initializations

    brew = HomebrewRelated.new
    python = PyenvRelated.new
end

# Excute main
main
