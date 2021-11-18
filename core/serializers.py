from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Car
    fields = ('id', 'plate', 'year', 'brand', 'color')

class CarDetailSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Car
    fields = ('id', 'plate', 'year', 'brand', 'color')

class ProfileSerializer(serializers.ModelSerializer):
  phone_number = serializers.CharField(source='profile.phone_number')
  
  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']

  def save(self, **kwargs):
    profile = self.validated_data.pop('profile')
    instance = super().save(**kwargs)
    Profile.objects.update_or_create(user=instance, defaults=profile)
    return instance