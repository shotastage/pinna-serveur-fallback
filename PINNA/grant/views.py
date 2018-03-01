"""
PINNA
views.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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
    def get(self, request, format=None):
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
