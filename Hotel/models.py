from django.db import models

# Create your models here.
class Room(models.Model):
    number=models.IntegerField()
    is_availble = models.BooleanField(default=True)

