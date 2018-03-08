"""
PINNA
urls.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.urls import path
from django.views import generic
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import DeviceCredentialCreateView, DeviceCredentialDestroyView, SignupView

urlpatterns = [

    # Registration API
    path("signup/", SignupView.as_view(), name = 'signup'),

    # Routings for JWT auth
    path("jwt/create/", TokenObtainPairView.as_view(), name = 'jwt-create'),
    path("jwt/refresh/", TokenRefreshView.as_view(), name = 'jwt-refresh'),
    path("jwt/verify/", TokenVerifyView.as_view(), name = 'token_verify'),

    # Routings for DCA (Device Credential Auth)
    path("dca/create/", DeviceCredentialCreateView.as_view(), name = 'jwt-create'),
    path("dca/destroy/", DeviceCredentialDestroyView.as_view(), name = 'jwt-create'),

    # Routings for ACA (API Credential Auth)
]
