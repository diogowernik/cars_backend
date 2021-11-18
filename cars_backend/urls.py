from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/cars/', views.CarList.as_view()),
    path('api/cars/<pk>', views.CarDetail.as_view()),

    path('api/clients/', views.UserList.as_view()),

]
