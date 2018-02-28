#!/usr/bin/env python

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
    app.debug = True
    app.run(host = "127.0.0.1", port = 1234)
