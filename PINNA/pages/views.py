"""
PINNA
views.py

Created by Shota Shimazu on 2018/03/01

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
"""

from django.shortcuts import render
from django.views import View
from pages.models import ServingPages


class Landings(View):

    template = "index.html"

    def render_template(self):

        serving_pages = ServingPages.objects.order_by('date').reverse().first()

        if not serving_pages.template_path is None:
            self.template = serving_pages.template_path
        else:
            self.template = "index.html"


    def get(self, request):

        # Fetch from pages database
        self.render_template()
        
        return render(request, self.template)

    def post(self, request):

        # Fetch from pages database
        self.render_template()

        return render(request, self.template)
