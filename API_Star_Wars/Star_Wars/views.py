from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person
from django.shortcuts import render

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('Name')
    serializers_class = PersonSerializer