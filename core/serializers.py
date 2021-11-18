from rest_framework import serializers
from . import models

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Car
    fields = ('id', 'plate', 'year', 'brand', 'color')

# class CarDetailSerializer(serializers.ModelSerializer):
  
#   class Meta:
#     model = models.Car
#     fields = ('id', 'plate', 'year', 'brand', 'color')