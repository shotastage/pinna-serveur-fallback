#!/usr/bin/env ruby

"""
PINNA
migration_to_new_gitlab.rb

Created by Shota Shimazu on 2018/03/15

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""


current_origin_url = `git config --get remote.origin.url`

puts "Current origin: " + current_origin_url

if current_origin_url == "git@hplab.work:pinna-music/pinna-music.git"
    sepa = current_origin_url.split("@")
    new_origin_url = sepa[0] + "@" + "git." + sepa[1]
    puts "New origin: " + new_origin_url

    # Set new origin URL
    system("git remote rm origin")
    system("git remote add origin " + new_origin_url)
end

system("git remote rm origin")
system("git remote add origin git@git.hplab.work:pinna-music/pinna-serveur.git")
