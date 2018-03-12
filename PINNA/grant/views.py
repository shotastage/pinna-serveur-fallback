"""
PINNA
views.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.views import View
from django.contrib.auth.models import User
from rest_framework import authentication, permissions, generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import (SignupVerification, DeviceCredential)




class SignupView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    serializer_class   = UserSerializer

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupVerificationView(View):
    
    def get(self, request):

        pending = SignupVerification.objects.filter( verification_code = request.GET.get("code"))

        if not pending.is_revoked:
            user = User.objects.filter( email = pending.email)
            user.is_active = True
            user.save()


    def post(self):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




class DeviceCredentialCreateView(APIView):
    def get(self, request, format=None):
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceCredentialDestroyView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
