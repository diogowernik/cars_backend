# import json
# from rest_framework import permissions
# from . import models

# class IsOwnerOrReadOnly(permissions.BasePermission):
  
#   def has_object_permission(self, request, view, obj):
#     # Read permissions are allowed to any request,
#     # so we'll always allow GET, HEAD or OPTIONS requests.
#     if request.method in permissions.SAFE_METHODS:
#         return True

#     # Write permissions are only allowed to the owner of the car.
#     return obj.owner == request.user

# class CarOwnerOrReadOnly(permissions.BasePermission):
  
#   def has_object_permission(self, request, view, obj):
#     # Read permissions are allowed to any request,
#     # so we'll always allow GET, HEAD or OPTIONS requests.
#     if request.method in permissions.SAFE_METHODS:
#         return True

#     # Write permissions are only allowed to the owner of the car.
#     return obj.car.owner == request.user

#   def has_permission(self, request, view):
#     try:
#       if request.method == "POST":
#         # For create action
#         data = json.loads(request.body)
#         models.Car.objects.get(pk=data["car"], owner_id=request.user.id)
#       return True
#     except:
#       return False