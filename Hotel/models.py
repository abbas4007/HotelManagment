from django.db import models

class Room(models.Model):
    number=models.IntegerField(max_length=3)
    is_availble = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        self.is_availble =False
        super(Room,self).save(*args,**kwargs)

class Person(models.Model):
    name= models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    date_subscribed = models.DateTimeField(auto_now=True)
    messages_received = models.IntegerField()