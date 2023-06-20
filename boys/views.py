from django.shortcuts import render
from rest_framework import generics
from boys.models import Boys
from .serializers import BoysSerializer


# Create your views here.
class BoysView(generics.ListAPIView):
    queryset = Boys.objects.all()
    serializer_class = BoysSerializer
