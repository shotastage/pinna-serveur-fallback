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
from pages.models import ServingPages


class Landings(View):

    template = "index.html"

    def render_template(self):

        serving_pages = ServingPages.objects.all()

        for i in range(len(serving_pages)):
            list_item = serving_pages[i]
            print('{0}:{1}'.format(i, list_item))

        self.template = "index.html"


    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        return render(request, self.template)
