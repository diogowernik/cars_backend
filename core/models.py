from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  plate = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

  def __str__(self):
    return "{}/{}".format(self.owner.username, self.name)
