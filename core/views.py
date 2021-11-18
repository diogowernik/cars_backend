# Create your views here.

from rest_framework import generics
from . import models, serializers, permissions

class CarList(generics.ListCreateAPIView):
  serializer_class = serializers.CarSerializer

  def get_queryset(self):
    return models.Car.objects.filter(owner_id=self.request.user.id)

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsOwnerOrReadOnly]
  serializer_class = serializers.CarDetailSerializer
  queryset = models.Car.objects.all()
