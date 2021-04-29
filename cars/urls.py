from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from cars import views

router = routers.DefaultRouter() 
router.register(r'cars', views.CarViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
