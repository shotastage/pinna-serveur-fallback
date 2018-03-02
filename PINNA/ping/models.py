from django.db import models

# Create your models here.


class Pings(models.Model):
  pingid      = models.UUIDField(primary_key = True)
  lat         = models.CharField(max_length = 255)
  lng         = models.CharField(max_length = 255)
  timestamp   = models.DateField()
  title       = models.CharField(max_length = 255)
  description = models.TextField(blank = True)
  created_by  = models.CharField(max_length = 255)
  on_deletion = models.BooleanField(default = False)
  is_private  = models.BooleanField(default = False)
  pin_type    = models.CharField(max_length = 255)
  re_pin      = models.IntegerField(default = 0)


class PingsSongDetail(Pings):
  song_id       = models.UUIDField()
  song_title         = models.CharField(max_length = 255)
  artist_id     = models.UUIDField()
  artist        = models.CharField(max_length = 255)
  genre         = models.CharField(max_length = 255)
  release_date  = models.DateField()
  recorded_on   = models.CharField(max_length = 255)
  favorites     = models.IntegerField()
  is_hidden     = models.BooleanField()


class CompositionDetail(PingsSongDetail):
  composer_id           = models.UUIDField()
  composer              = models.CharField(max_length = 255)
  composer_birthday     = models.DateField()
  composer_birthplace   = models.CharField(max_length = 255)
  composer_living_place = models.CharField(max_length = 255)
  composed_place        = models.CharField(max_length = 255)
  composed_when         = models.DateTimeField()
