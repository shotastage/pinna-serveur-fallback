#!/usr/bin/env ruby

"""
PINNA
uninstall_mac.rb

Created by Shota Shimazu on 2018/03/12

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

require 'rbconfig'
require 'tmpdir'
require 'fileutils'


class UninstallRecetPostgreApp
    def initialize
        remove()
    end

    def remove
        puts "Removing Postgre.app ..."
        Dir.chdir("/Applications/")
        system("rm -rf Postgres.app")
    end
end

class UninstallBrewPackages

    def initialize
        #puts "Uninstalling brew packages..."
        #system("brew uninstall yarn node pyenv")
    end

end


def main

    puts "This script is now under construction!"

    UninstallRecetPostgreApp.new
    UninstallBrewPackages.new
end

main
