"""
PINNA Serveur
admin.py

Created by Shota Shimazu on 2018/2/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.contrib import admin
from .models import OptimizationSchedule


class OptimizationScheduleAdmin(admin.ModelAdmin):
    readonly_fields = (
        "optimization_id",
    )

admin.site.register(OptimizationSchedule, OptimizationScheduleAdmin)
