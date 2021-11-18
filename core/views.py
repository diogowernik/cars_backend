# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from . import models, serializers, permissions

class CarList(generics.ListCreateAPIView):
  serializer_class = serializers.CarSerializer

  def get_queryset(self):
    return models.Car.objects.filter(owner_id=self.request.user.id).filter(is_active=True)

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class DeletedCarsList(generics.ListCreateAPIView):
  serializer_class = serializers.CarSerializer

  def get_queryset(self):
    return models.Car.objects.filter(owner_id=self.request.user.id).filter(is_active=False)

class CarDetail(generics.RetrieveUpdateAPIView):
  permission_classes = [permissions.IsOwnerOrReadOnly]
  serializer_class = serializers.CarDetailSerializer
  queryset = models.Car.objects.all()

class UserList(generics.ListCreateAPIView):
  serializer_class = serializers.UserSerializer

  def get_queryset(self):
    return models.User.objects.filter(email=self.request.user.id)

  def post(self, request, format=None):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
