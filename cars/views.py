from django.shortcuts import render
from rest_framework import viewsets
from cars.models import Cars
from cars.serializers import CarSerializer
from cars import CaML
from rest_framework.response import Response

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all().order_by('-id')
    serializer_class = CarSerializer
    def create(self, request, *args, **kwargs):
        super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
        ob = Cars.objects.latest('id')
        y = CaML.pred(ob)
        return Response({"status": "Success", "Price": y, 'tmp': args})  # Your override
from django.shortcuts import render

# Create your views here.
