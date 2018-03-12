"""
PINNA
models.py

Created by Shota Shimazu on 2018/02/25

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of RESTRICTED, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from secrets import token_urlsafe, compare_digest
from uuid import uuid4


class GrantUser(models.Model):

  ACCOUNT_TYPE = (
    ('normal', 'Normal Type Account'),
    ('admin', 'Administrator'),
    ('guest', 'Guest Account'),
    ('super', 'Super User Account'),
  )

  GENDER = (
    (0, 'Not Defined'),
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Other')
  )

  """
  user                  Relation to Django user model
  account_id            Grant account unique UUID
  account_secret        URL-safe 64 bit token for API verification secret
  account_type          Account types defined in ACCOUNT_TYPE
  """

  user            = models.OneToOneField(User, on_delete = models.CASCADE)
  account_id      = models.UUIDField(default = uuid4)
  account_secret  = models.CharField(max_length = 255)
  account_type    = models.CharField(max_length = 10, choices = ACCOUNT_TYPE, default="normal")

  """
  User Profile:

  phone                 Phone number
  country               Country user lives in
  address               User address ( real address )
  gender                Gender defined in GENDER
  profession            User profession
  """

  phone           = models.CharField(max_length = 255)
  country         = models.CharField(max_length = 255)
  bio             = models.TextField(blank = True)
  birthday        = models.DateField(blank = True)
  address         = models.CharField(max_length = 500, blank = True)
  gender          = models.IntegerField(choices = GENDER, default = 0)
  profession      = models.CharField(max_length = 255, blank = True)

  """
  User Settings:
  """
  is_onetap_login_enabled = models.BooleanField(default = False)


  def create(self):
    self.account_secret = token_urlsafe(64)


class DeviceCredential(models.Model):
  """
  ID                    device unique UUID
  credential            URL-safe 64 bit token
  device_name           Device name (e.g, SHOTA's iPhone7)
  useragent             Useragent like browser (e.g. Macintosh; Intel Mac OS X 10_13_3 Web/3.1)
  is_revoked            Boolean value whether the token is revoked or not
  """

  id            = models.UUIDField(primary_key = True, default = uuid4)
  credential    = models.CharField(max_length = 255)
  device_name   = models.CharField(max_length = 255)
  useragent     = models.CharField(max_length = 255)
  is_revoked    = models.BooleanField(default = False)


  def create(self):
    self.credential = token_hex(32)

  def update(self):
    self.create()

  def certificate(self, credential):
    return compare_digest(credential, self.credential)

  def revoke(self):
    self.is_revoked = True


class SignupVerification(models.Model):
  """
  email                 New registration email address
  created_on            Date & time of registering on pending
  verification_code     URL-safe token to verificate a registration
  is_revoked            Boolean value whether the verification code is revoked or not
  """

  email             = models.EmailField(unique = True)
  created_on        = models.DateTimeField(default = timezone.now)
  verification_code = models.CharField(max_length = 255)
  is_revoked        = models.BooleanField(default = False)

  def create(self):
    self.verification_code = token_urlsafe(64)



class OneTapLogin(models.Model):
  """
  token                 URL-safe token to verificate a one tap tapping!
  is_tapped             Boolean value whether the "one tap" is tapped or not
  is_revoked            Boolean value whether the verification code is revoked or not
  created_on            Date & time of one tap session
  """
  
  token       = models.CharField(max_length = 255)
  is_tapped   = models.BooleanField(default = False)
  is_revoked  = models.BooleanField(default = False)
  created_on  = models.DateTimeField(default = timezone.now)

  def create(self):
    self.token = token_urlsafe(64)


class PendingResetAccount(models.Model):
  account_id = models.UUIDField(unique = True)
  created_on = models.DateTimeField(default = timezone.now)
  is_revoked = models.BooleanField(default = False)
