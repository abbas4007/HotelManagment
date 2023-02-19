from django.db import models

# Create your models here.
class Room(models.Model):
    number=models.IntegerField(max_length=3)
    is_availble = models.BooleanField(default=True)
