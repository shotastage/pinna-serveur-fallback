from django.db import models

# Create your models here.


class User(models.Model):
  user_name = models.CharField()
  email = models.CharField()
