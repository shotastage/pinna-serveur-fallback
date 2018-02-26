from django.db import models

# Create your models here.


class Lambda(models.Model):
  """
  Models docstring is here.
  """
  id          = models.UUIDField(primary_key = True)
  registry_id = models.CharField(max_length = 255)
  title       = models.CharField(max_length = 255)
  version     = models.CharField(max_length = 255)
  author      = models.CharField(max_length = 255)
