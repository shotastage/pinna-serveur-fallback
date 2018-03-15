/*
PINNA
preinstall-script.js

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
*/

if (process.env.npm_execpath.indexOf('yarn') === -1) {
    console.error('You must use Yarn to install dependencies:');
    console.error('  $ yarn install');
    process.exit(1);
}
