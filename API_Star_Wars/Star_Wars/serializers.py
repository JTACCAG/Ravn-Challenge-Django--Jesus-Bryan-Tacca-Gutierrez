from rest_framework import serializers
from .models import Person, People, Vehicles

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('Name', 'Birth_Year', 'Eye_Color', 'Gender', 'Height')
class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('Name', 'Class', 'Crew')