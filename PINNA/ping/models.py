from django.db import models

# Create your models here.


class Pings(models.Model):
  pingid      = models.CharField(max_length = 35, primary_key = True)
  lat         = models.CharField(max_length = 35)
  lng         = models.CharField(max_length = 35)
  timestamp   = models.CharField(max_length = 35)
  mainstream  = models.CharField(max_length = 35)
  substream   = models.CharField(max_length = 35)
  playtype    = models.CharField(max_length = 35)


class PingsSongInfo(models.Model):
  pingid      = models.CharField(max_length = 35, primary_key = True)
  title       = models.CharField()
  artist      = models.CharField()
  composer    = models.CharField()
  year        = models.CharField()

