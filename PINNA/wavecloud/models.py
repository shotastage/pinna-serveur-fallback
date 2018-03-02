from django.db import models

# Create your models here.


class SoundCloudIndexing(models.Model):
  song_id = models.UUIDField()
  url = models.URLField()
