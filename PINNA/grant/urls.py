"""
PINNA
urls.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.conf.urls import url
from django.views import generic
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import DeviceCredentialCreateView, DeviceCredentialDestroyView

urlpatterns = [
    # Rootings for JWT auth
    url(r'^jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    url(r'^jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    url(r'^jwt/verify/$', TokenVerifyView.as_view(), name='token_verify'),

    # Routings for DCA (Device Credential Auth)
    url(r'^dca/create/', DeviceCredentialCreateView.as_view(), name='jwt-create'),
    url(r'^dca/destroy/', DeviceCredentialDestroyView.as_view(), name='jwt-create'),
]
