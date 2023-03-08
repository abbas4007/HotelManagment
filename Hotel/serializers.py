from rest_framework import serializers
from .models import Room

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('number',)