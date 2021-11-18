from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  plate = models.CharField(max_length=100)
  number_of_tables = models.IntegerField(default=1)
  year = models.CharField(max_length=100, blank=True)
  brand = models.CharField(max_length=100, blank=True)
  color = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return "{}/{}".format(self.owner.username, self.plate)
