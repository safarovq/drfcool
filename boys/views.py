from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from boys.models import Boys
from .serializers import BoysSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# class BoysView(generics.ListAPIView):
#     queryset = Boys.objects.all()
#     serializer_class = BoysSerializer


class BoysAPIView(APIView):
    def get(self, request):
        lst = Boys.objects.all().values()

        return Response({'name': list(lst)})

    def post(self, request):
        new_post = Boys.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            category_id=request.data['category_id'],
        )

        return Response({'new_post': model_to_dict(new_post)})
