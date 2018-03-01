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



class Landings(View):
    def get(self, request):
        return render(request, 'index.html')


    def post(self, request):
        return render(request, 'index.html')
