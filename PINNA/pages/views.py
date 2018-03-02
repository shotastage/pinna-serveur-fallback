"""
PINNA
views.py

Created by Shota Shimazu on 2018/03/01

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ServingPages


class Landings(View):

    template = "index.html"

    def render_template(self):
        obj = ServingPages.__str__()

        self.template = "index.html"

    def get(self, request):
        return render(request, self.template)


    def post(self, request):
        return render(request, self.template)
