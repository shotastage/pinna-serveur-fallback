#!/usr/bin/env sh
#
# PINNA
# Validation_ubuntu_python_before_script.sh
#
# Created by Shota Shimazu on 2018/03/13
#
# Copyright (c) 2018 Shota Shimazu All Rights Reserved.
#
# This software is released under the terms of restricted, see LICENSE for detail.
# https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
#

apt-get update
apt-get install -y curl build-essential git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev
apt-get install -y python3-tk tk-dev python-tk libfreetype6-dev 
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
pyenv --version
pyenv install 3.6.4
pyenv global 3.6.4
pip install pipenv
pipenv --three
pipenv install
pipenv install --dev
