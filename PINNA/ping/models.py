from django.db import models

# Create your models here.


class Pings(models.Model):
  pingid      = models.CharField(max_length = 35, primary_key = True)
  lat         = models.CharField(max_length = 255)
  lng         = models.CharField(max_length = 255)
  timestamp   = models.CharField(max_length = 255)
  mainstream  = models.CharField(max_length = 255)
  substream   = models.CharField(max_length = 255)
  playtype    = models.CharField(max_length = 255)


class PingsSongInfo(models.Model):
  pingid      = models.CharField(max_length = 35, primary_key = True)
  title       = models.CharField(max_length = 255)
  artist      = models.CharField(max_length = 255)
  composer    = models.CharField(max_length = 255)
  year        = models.CharField(max_length = 255)
