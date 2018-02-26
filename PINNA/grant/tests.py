"""
PINNA
tests.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.test import TestCase
from grant.models import DeviceCredential
# Create your tests here.


class DeviceCredentialModelTests(TestCase):
    def test_is_empty(self):
        obj = DeviceCredential.objects.all()
        self.assertEqual(obj.count(), 0)
