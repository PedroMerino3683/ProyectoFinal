from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import ClimaSerializer
from .models import Clima

# Create your views here.
class ClimaViewSet(ModelViewSet):
    serializer_class = ClimaSerializer
    queryset = Clima.objects.all()