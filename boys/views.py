from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from boys.models import Boys, Category
from .serializers import BoysSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
# class BoysView(generics.ListAPIView):
#     queryset = Boys.objects.all()
#     serializer_class = BoysSerializer

class BoysViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    # queryset = Boys.objects.all()
    serializer_class = BoysSerializer

    #     @action(methods=['get'], detail=False)
    #     def category(self, request):
    #         cat = Category.objects.all()
    #         return Response({'categories': (c.name for c in cat)})
    #
    # #
    def get_queryset(self):
        return Boys.objects.all()[:2]

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cat = Category.objects.get(pk=pk)
        return Response({'categories': cat.name})

#
# class BoysListAPIView(generics.ListCreateAPIView):
#     queryset = Boys.objects.all()
#     serializer_class = BoysSerializer
#
#
# class BoysUpdateAPIView(generics.UpdateAPIView):
#     queryset = Boys.objects.all()
#     serializer_class = BoysSerializer
#
#
# class BoysCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Boys.objects.all()
#     serializer_class = BoysSerializer

# class BoysAPIView(APIView):
#     def get(self, request):
#         # lst = Boys.objects.all().values()
#         b = Boys.objects.all()
#
#         return Response({'name': BoysSerializer(b, many=True).data})
#
#     def post(self, request):
#         serializer = BoysSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'new_post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'no method put'})
#
#         try:
#             instance = Boys.objects.get(pk=pk)
#         except:
#             return Response({'error': 'object does not exist'})
#
#         serializer = BoysSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'no method delete'})
#
#         try:
#             instance = Boys.objects.get(pk=pk)
#         except:
#             return Response({'error': 'object does not exist'})
#
#         instance.delete()
#
#         return Response({'message': 'deleted'})
