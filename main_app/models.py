from django.db import models

# Create your models here.
class Queero(models.Model):
  name = models.CharField(max_length=100)
  occupation = models.TextField(max_length=2000)
  biography = models.TextField(max_length=2000)
  legacy = models.TextField(max_length=2000)
  


