from django.db import models

# Create your models here.


class Pings(models.Model):
  pingid      = models.CharField(max_length = 35, primary_key = True)
  lat         = models.CharField()
  lng         = models.CharField()
  timestamp   = models.CharField()
  mainstream  = models.CharField()
  substream   = models.CharField()
