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

class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrWriteOnly,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
