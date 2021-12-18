from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import routers
from .serializers import PersonSerializer
from .models import Person
from django.shortcuts import render

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('Name')
    serializer_class = PersonSerializer