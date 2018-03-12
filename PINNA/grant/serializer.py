"""
PINNA
serializer.py

Created by Shota Shimazu on 2018/03/08

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import (DeviceCredential,)


class DeviceCredentialSerializer(serializers.ModelSerializer):
    
    device_name = serializers.CharField(max_length = 255)
    useragent = serializers.CharField(max_length = 255)

    def create(self, validated_data):
        credential = DeviceCredential.objects.create()
        return credential

    class Meta:
        model = DeviceCredential
        fields = ("credential", "name", "os")


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset = User.objects.all())]
    )
    username = serializers.CharField(
        validators = [UniqueValidator(queryset = User.objects.all())]
    )
    password = serializers.CharField(min_length = 8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data["username"], validated_data["email"],
             validated_data["password"])
        user.is_active = False
        user.save()
    
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
