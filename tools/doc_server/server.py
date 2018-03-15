#!/usr/bin/env python
"""
PINNA
server.py

Created by Shota Shimazu on 2018/03/01

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def index():
    return "PINNA Development Documentation"

@app.route("/api/")
def app_view():
    os.listdir("../")
    return render_template('api.html')

if __name__ == "__main__":
    print("Launching documentation server...")
    app.debug = True
    app.run(host = "127.0.0.1", port = 1234)
