#!/usr/bin/env sh
#
# PINNA
# codeclimate_script.sh
#
# Created by Shota Shimazu on 2018/03/13
# 
# Copyright (c) 2018 Shota Shimazu All Rights Reserved.
# 
# This software is released under the terms of restricted, see LICENSE for detail.
# https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
#

apk update && apk add jq
./scripts/codequality analyze -f json > raw_codeclimate.json || true
# The following line keeps only the fields used in the MR widget, reducing the JSON artifact size
jq -c 'map({check_name,description,fingerprint,location})' raw_codeclimate.json > codeclimate.json
