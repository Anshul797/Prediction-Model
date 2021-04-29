from rest_framework import serializers
from cars.models import Cars
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ('name', 'seller', 'offerType' ,   'abtest' ,   'vehicleType' ,   'yearOfRegistration',    'gearbox',    'powerPS',    'model',    'kilometer',    'monthOfRegistration','fuelType','brand','notRepairedDamage','postalCode','nrOfPictures')
